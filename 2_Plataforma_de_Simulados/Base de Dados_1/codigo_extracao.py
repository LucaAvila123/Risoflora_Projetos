# TODO: alterar os arquivos JSON para não colocar a imagem como imperante das questões inteiras

import fitz  # PyMuPDF
import shutil
import json
import re
import os
import pandas as pd

def processar_enem(caminho_pdf, endereco_imagens, caminho_gabarito, ano):
    doc = fitz.open(caminho_pdf)
    resultado = {"prova": f"ENEM {ano}", "questoes": []}
    if os.path.exists(endereco_imagens):
        shutil.rmtree(endereco_imagens)
    
    os.makedirs(endereco_imagens)
    df = pd.read_csv(caminho_gabarito)
    this_id = 1
    
    for num_pag in range(len(doc)):
        pagina = doc.load_page(num_pag)
        
        # 1. Extração de Imagens com conversão adequada
        imagens_da_pagina = []
        for img_idx, img in enumerate(pagina.get_images()):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                
                # Verifica se precisa converter
                if pix.colorspace is not None:
                    # Se não for RGB ou Grayscale, converte para RGB
                    if pix.colorspace.name not in [fitz.csRGB.name, fitz.csGRAY.name]:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                
                # Se for imagem com máscara/alpha, converte
                if pix.alpha:
                    pix = fitz.Pixmap(pix, 0)  # Remove canal alpha
                
                nome_img = f"pag{num_pag+1}_img{img_idx}.png"
                pix.save(os.path.join(endereco_imagens, nome_img))
                imagens_da_pagina.append(nome_img)
                
            except Exception as e:
                print(f"Erro ao extrair imagem na pág {num_pag+1}, img {img_idx}: {str(e)}")
                # Tenta uma abordagem alternativa se falhar
                try:
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    # Força conversão para RGB
                    pix_converted = fitz.Pixmap(fitz.csRGB, pix)
                    nome_img = f"pag{num_pag+1}_img{img_idx}_convertida.png"
                    pix_converted.save(os.path.join(endereco_imagens, nome_img))
                    imagens_da_pagina.append(nome_img)
                except Exception as e2:
                    print(f"Falha na tentativa alternativa: {e2}")
            finally:
                # Limpa a memória
                if 'pix' in locals():
                    pix = None
                if 'pix_converted' in locals():
                    pix_converted = None

        # 2. Extração de Texto com Regex melhorado
        texto = pagina.get_text("text")
        # Procura por "QUESTÃO" seguido de números, ignorando maiúsculas/minúsculas
        blocos = re.split(r'(?i)QUESTÃO\s+(\d+)', texto)
        
        if len(blocos) > 1:
            for i in range(1, len(blocos), 2):
                num_q = blocos[i]
                conteudo = blocos[i+1]
                
                # Verifica se o ID existe no gabarito
                if this_id in df['ID'].values:
                    gabarito_letra = df.loc[df['ID'] == this_id]['Gabarito'].values[0]
                else:
                    gabarito_letra = "N/A"
                    print(f"Aviso: ID {this_id} não encontrado no gabarito")

                # Identificar alternativas A, B, C, D, E no final das questões
                alternativas = {}
                regex_alt = r'\n\s*([A-E])\s+(.*?)(?=\n\s*[A-E]\s+|$)'
                matches = re.findall(regex_alt, conteudo, re.DOTALL)
                
                for letra, desc in matches:
                    alternativas[letra] = desc.strip().replace('\n', ' ')

                # Limpar enunciado: remove o que for alternativa
                enunciado = re.split(r'\n\s*A\s+', conteudo)[0].strip()

                resultado["questoes"].append({
                    "numero": int(num_q),
                    "pagina": num_pag + 1,
                    "enunciado": enunciado,
                    "alternativas": alternativas,
                    "imagens": imagens_da_pagina if len(alternativas) > 0 else [],
                    "gabarito": gabarito_letra
                })
                this_id += 1
                
    return resultado

# Execução
lista_pastas = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
for ano in lista_pastas:
    try:
        print(f"\nProcessando ENEM {ano}...")
        
        # Processa dia 1
        dados_1_dia = processar_enem(
            f"./ENEM_{ano}/{ano}_PV_impresso_D1_CD1.pdf", 
            f"./ENEM_{ano}/imagens_extraidas_1", 
            f"./ENEM_{ano}/gabarito_{ano}_dia_1.csv", 
            ano
        )
        with open(f"./ENEM_{ano}/enem_{ano}_1_dia.json", "w", encoding="utf-8") as f:
            json.dump(dados_1_dia, f, ensure_ascii=False, indent=4)
        print(f"Dia 1: Sucesso! {len(dados_1_dia['questoes'])} questões extraídas.")

        # Processa dia 2
        dados_2_dia = processar_enem(
            f"./ENEM_{ano}/{ano}_PV_impresso_D2_CD5.pdf", 
            f"./ENEM_{ano}/imagens_extraidas_2", 
            f"./ENEM_{ano}/gabarito_{ano}_dia_2.csv", 
            ano
        )
        with open(f"./ENEM_{ano}/enem_{ano}_2_dia.json", "w", encoding="utf-8") as f:
            json.dump(dados_2_dia, f, ensure_ascii=False, indent=4)
        print(f"Dia 2: Sucesso! {len(dados_2_dia['questoes'])} questões extraídas.")

    except Exception as e:
        print(f"Erro fatal no ano {ano}: {e}")
        import traceback
        traceback.print_exc()