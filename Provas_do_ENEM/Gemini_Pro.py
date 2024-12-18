# Bibliotecas
import google.generativeai as genai

# Chave
genai.configure(api_key="-------------------------------------------------------")

# Modelo
model1 = genai.GenerativeModel(model_name="models/gemini-1.5-pro-002")
model2 = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Path dos arquivos

ENEM_2013 =['Provas_do_ENEM\\ENEM\\2013\\1.jpg','Provas_do_ENEM\\ENEM\\2013\\2.jpg','Provas_do_ENEM\\ENEM\\2013\\3.jpg','Provas_do_ENEM\\ENEM\\2013\\4.jpg','Provas_do_ENEM\\ENEM\\2013\\5.jpg',
            'Provas_do_ENEM\\ENEM\\2013\\6.jpg','Provas_do_ENEM\\ENEM\\2013\\7.jpg','Provas_do_ENEM\\ENEM\\2013\\8.jpg','Provas_do_ENEM\\ENEM\\2013\\9.jpg','Provas_do_ENEM\\ENEM\\2013\\10.jpg',
            'Provas_do_ENEM\\ENEM\\2013\\11.jpg','Provas_do_ENEM\\ENEM\\2013\\12.jpg','Provas_do_ENEM\\ENEM\\2013\\13.jpg']

ENEM_2014 =['Provas_do_ENEM\\ENEM\\2014\\1.jpg','Provas_do_ENEM\\ENEM\\2014\\2.jpg','Provas_do_ENEM\\ENEM\\2014\\3.jpg','Provas_do_ENEM\\ENEM\\2014\\4.jpg','Provas_do_ENEM\\ENEM\\2014\\5.jpg',
            'Provas_do_ENEM\\ENEM\\2014\\6.jpg','Provas_do_ENEM\\ENEM\\2014\\7.jpg','Provas_do_ENEM\\ENEM\\2014\\8.jpg','Provas_do_ENEM\\ENEM\\2014\\9.jpg','Provas_do_ENEM\\ENEM\\2014\\10.jpg',
            'Provas_do_ENEM\\ENEM\\2014\\11.jpg','Provas_do_ENEM\\ENEM\\2014\\12.jpg','Provas_do_ENEM\\ENEM\\2014\\13.jpg']

ENEM_2015 = ['Provas_do_ENEM\\ENEM\\2015\\1.jpg','Provas_do_ENEM\\ENEM\\2015\\2.jpg','Provas_do_ENEM\\ENEM\\2015\\3.jpg','Provas_do_ENEM\\ENEM\\2015\\4.jpg','Provas_do_ENEM\\ENEM\\2015\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2015\\6.jpg','Provas_do_ENEM\\ENEM\\2015\\7.jpg','Provas_do_ENEM\\ENEM\\2015\\8.jpg','Provas_do_ENEM\\ENEM\\2015\\9.jpg','Provas_do_ENEM\\ENEM\\2015\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2015\\11.jpg','Provas_do_ENEM\\ENEM\\2015\\12.jpg','Provas_do_ENEM\\ENEM\\2015\\13.jpg']

ENEM_2016 = ['Provas_do_ENEM\\ENEM\\2016\\1.jpg','Provas_do_ENEM\\ENEM\\2016\\2.jpg','Provas_do_ENEM\\ENEM\\2016\\3.jpg','Provas_do_ENEM\\ENEM\\2016\\4.jpg','Provas_do_ENEM\\ENEM\\2016\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2016\\6.jpg','Provas_do_ENEM\\ENEM\\2016\\7.jpg','Provas_do_ENEM\\ENEM\\2016\\8.jpg','Provas_do_ENEM\\ENEM\\2016\\9.jpg','Provas_do_ENEM\\ENEM\\2016\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2016\\11.jpg','Provas_do_ENEM\\ENEM\\2016\\12.jpg','Provas_do_ENEM\\ENEM\\2016\\13.jpg','Provas_do_ENEM\\ENEM\\2016\\14.jpg','Provas_do_ENEM\\ENEM\\2016\\15.jpg']

ENEM_2017 = ['Provas_do_ENEM\\ENEM\\2017\\1.jpg','Provas_do_ENEM\\ENEM\\2017\\2.jpg','Provas_do_ENEM\\ENEM\\2017\\3.jpg','Provas_do_ENEM\\ENEM\\2017\\4.jpg','Provas_do_ENEM\\ENEM\\2017\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2017\\6.jpg','Provas_do_ENEM\\ENEM\\2017\\7.jpg','Provas_do_ENEM\\ENEM\\2017\\8.jpg','Provas_do_ENEM\\ENEM\\2017\\9.jpg','Provas_do_ENEM\\ENEM\\2017\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2017\\11.jpg','Provas_do_ENEM\\ENEM\\2017\\12.jpg','Provas_do_ENEM\\ENEM\\2017\\13.jpg','Provas_do_ENEM\\ENEM\\2017\\14.jpg','Provas_do_ENEM\\ENEM\\2017\\15.jpg',
             'Provas_do_ENEM\\ENEM\\2017\\16.jpg']

ENEM_2018 = ['Provas_do_ENEM\\ENEM\\2018\\1.jpg','Provas_do_ENEM\\ENEM\\2018\\2.jpg','Provas_do_ENEM\\ENEM\\2018\\3.jpg','Provas_do_ENEM\\ENEM\\2018\\4.jpg','Provas_do_ENEM\\ENEM\\2018\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2018\\6.jpg','Provas_do_ENEM\\ENEM\\2018\\7.jpg','Provas_do_ENEM\\ENEM\\2018\\8.jpg','Provas_do_ENEM\\ENEM\\2018\\9.jpg','Provas_do_ENEM\\ENEM\\2018\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2018\\11.jpg','Provas_do_ENEM\\ENEM\\2018\\12.jpg','Provas_do_ENEM\\ENEM\\2018\\13.jpg','Provas_do_ENEM\\ENEM\\2018\\14.jpg','Provas_do_ENEM\\ENEM\\2018\\15.jpg',
             'Provas_do_ENEM\\ENEM\\2018\\16.jpg']

ENEM_2019 = ['Provas_do_ENEM\\ENEM\\2019\\1.jpg','Provas_do_ENEM\\ENEM\\2019\\2.jpg','Provas_do_ENEM\\ENEM\\2019\\3.jpg','Provas_do_ENEM\\ENEM\\2019\\4.jpg','Provas_do_ENEM\\ENEM\\2019\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2019\\6.jpg','Provas_do_ENEM\\ENEM\\2019\\7.jpg','Provas_do_ENEM\\ENEM\\2019\\8.jpg','Provas_do_ENEM\\ENEM\\2019\\9.jpg','Provas_do_ENEM\\ENEM\\2019\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2019\\11.jpg','Provas_do_ENEM\\ENEM\\2019\\12.jpg','Provas_do_ENEM\\ENEM\\2019\\13.jpg','Provas_do_ENEM\\ENEM\\2019\\14.jpg','Provas_do_ENEM\\ENEM\\2019\\15.jpg']

ENEM_2020 = ['Provas_do_ENEM\\ENEM\\2020\\1.jpg','Provas_do_ENEM\\ENEM\\2020\\2.jpg','Provas_do_ENEM\\ENEM\\2020\\3.jpg','Provas_do_ENEM\\ENEM\\2020\\4.jpg','Provas_do_ENEM\\ENEM\\2020\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2020\\6.jpg','Provas_do_ENEM\\ENEM\\2020\\7.jpg','Provas_do_ENEM\\ENEM\\2020\\8.jpg','Provas_do_ENEM\\ENEM\\2020\\9.jpg','Provas_do_ENEM\\ENEM\\2020\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2020\\11.jpg','Provas_do_ENEM\\ENEM\\2020\\12.jpg','Provas_do_ENEM\\ENEM\\2020\\13.jpg','Provas_do_ENEM\\ENEM\\2020\\14.jpg','Provas_do_ENEM\\ENEM\\2020\\15.jpg',
             'Provas_do_ENEM\\ENEM\\2020\\16.jpg']

ENEM_2021= ['Provas_do_ENEM\\ENEM\\2021\\1.jpg','Provas_do_ENEM\\ENEM\\2021\\2.jpg','Provas_do_ENEM\\ENEM\\2021\\3.jpg','Provas_do_ENEM\\ENEM\\2021\\4.jpg','Provas_do_ENEM\\ENEM\\2021\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2021\\6.jpg','Provas_do_ENEM\\ENEM\\2021\\7.jpg','Provas_do_ENEM\\ENEM\\2021\\8.jpg','Provas_do_ENEM\\ENEM\\2021\\9.jpg','Provas_do_ENEM\\ENEM\\2021\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2021\\11.jpg','Provas_do_ENEM\\ENEM\\2021\\12.jpg','Provas_do_ENEM\\ENEM\\2021\\13.jpg','Provas_do_ENEM\\ENEM\\2021\\14.jpg','Provas_do_ENEM\\ENEM\\2021\\15.jpg']

ENEM_2022= ['Provas_do_ENEM\\ENEM\\2022\\1.jpg','Provas_do_ENEM\\ENEM\\2022\\2.jpg','Provas_do_ENEM\\ENEM\\2022\\3.jpg','Provas_do_ENEM\\ENEM\\2022\\4.jpg','Provas_do_ENEM\\ENEM\\2022\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2022\\6.jpg','Provas_do_ENEM\\ENEM\\2022\\7.jpg','Provas_do_ENEM\\ENEM\\2022\\8.jpg','Provas_do_ENEM\\ENEM\\2022\\9.jpg','Provas_do_ENEM\\ENEM\\2022\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2022\\11.jpg','Provas_do_ENEM\\ENEM\\2022\\12.jpg','Provas_do_ENEM\\ENEM\\2022\\13.jpg','Provas_do_ENEM\\ENEM\\2022\\14.jpg','Provas_do_ENEM\\ENEM\\2022\\15.jpg']

ENEM_2023= ['Provas_do_ENEM\\ENEM\\2023\\1.jpg','Provas_do_ENEM\\ENEM\\2023\\2.jpg','Provas_do_ENEM\\ENEM\\2023\\3.jpg','Provas_do_ENEM\\ENEM\\2023\\4.jpg','Provas_do_ENEM\\ENEM\\2023\\5.jpg',
             'Provas_do_ENEM\\ENEM\\2023\\6.jpg','Provas_do_ENEM\\ENEM\\2023\\7.jpg','Provas_do_ENEM\\ENEM\\2023\\8.jpg','Provas_do_ENEM\\ENEM\\2023\\9.jpg','Provas_do_ENEM\\ENEM\\2023\\10.jpg',
             'Provas_do_ENEM\\ENEM\\2023\\11.jpg','Provas_do_ENEM\\ENEM\\2023\\12.jpg','Provas_do_ENEM\\ENEM\\2023\\13.jpg','Provas_do_ENEM\\ENEM\\2023\\14.jpg','Provas_do_ENEM\\ENEM\\2023\\15.jpg',
             'Provas_do_ENEM\\ENEM\\2023\\16.jpg']
# Gemini - teste das questões

# Perguntas

pergunta2013_2 = {'Provas_do_ENEM\\ENEM\\2013\\1.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 136, 137 e 138 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\2.jpg': "Cada questão possui somente uma alternativa correta.Escolha a alternativa correta  para as questões 139, 140, 141 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\3.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 142 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\4.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 143, 144, 145, 146, 147 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\5.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 148, 149, 150, 151 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\6.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 152, 153, 154, 155 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\7.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 156, 157, 158, 159 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\8.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 160, 161, 162 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\9.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 163, 164, 165, 166, 167 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\10.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 168, 169, 170 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\11.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 171, 172, 173 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\12.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 174, 175, 176 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\13.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 177, 178, 179, 180 e justifique cada escolha detalhadamente."}

pergunta2013_3 = {'Provas_do_ENEM\\ENEM\\2013\\1.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 136, 137 e 138  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\2.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 139, 140, 141 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\3.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 142 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\4.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 143, 144, 145, 146, 147  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\5.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões  148, 149, 150, 151  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\6.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões   152, 153, 154, 155  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\7.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões  156, 157, 158, 159  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\8.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões  160, 161, 162  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\9.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões  163, 164, 165, 166, 167  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\10.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões  168, 169, 170  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\11.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões   171, 172, 173  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\12.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões   174, 175, 176  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2013\\13.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões   177, 178, 179, 180  detalhadamente."}

pergunta2014_2 = {'Provas_do_ENEM\\ENEM\\2014\\1.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 136, 137, 138 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\2.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 139, 140 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\3.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 141, 142, 143 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\4.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 144, 145, 146, 147 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\5.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 148, 149, 150 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\6.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 151, 152, 153 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\7.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 154, 155, 156 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\8.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 157, 158, 159 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\9.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 160, 161, 162, 163 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\10.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 164, 165, 166, 167 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\11.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 168, 169, 170, 171 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\12.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 172, 173, 174, 175, 176 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\13.jpg':"Cada questão possui somente uma alternativa correta.  Escolha a alternativa correta  para as questões 177, 178, 179, 180 e justifique cada escolha detalhadamente."}

pergunta2014_3 = {'Provas_do_ENEM\\ENEM\\2014\\1.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 136, 137, 138 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\2.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 139, 140  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\3.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 141, 142, 143  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\4.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 144, 145, 146, 147  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\5.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 148, 149, 150  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\6.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 151, 152, 153  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\7.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 154, 155, 156  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\8.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 157, 158, 159  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\9.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 160, 161, 162, 163  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\10.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 164, 165, 166, 167  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\11.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 168, 169, 170, 171  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\12.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 172, 173, 174, 175, 176  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2014\\13.jpg':"Cada questão possui somente uma alternativa correta.  Resolva as questões 177, 178, 179, 180  detalhadamente."}

pergunta2015_2 = {'Provas_do_ENEM\\ENEM\\2015\\1.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 136, 137, 138 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\2.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 139, 140, 141 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\3.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 142, 143 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\4.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 144, 145, 146, 147 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\5.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 148, 149, 150 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\6.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 151, 152, 153, 154, 155 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\7.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 156, 157, 158, 159 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\8.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 160, 161, 162, 163 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\9.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 164, 165 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\10.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 166, 167, 168, 169 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\11.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 170, 171, 172 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\12.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 173, 174, 175, 176 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\13.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 177, 178, 179, 180 e justifique cada escolha detalhadamente."}

pergunta2015_3 = {'Provas_do_ENEM\\ENEM\\2015\\1.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 136, 137, 138  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\2.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 139, 140, 141  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\3.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 142, 143  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\4.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 144, 145, 146, 147  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\5.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 148, 149, 150  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\6.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 151, 152, 153, 154, 155  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\7.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 156, 157, 158, 159  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\8.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 160, 161, 162, 163  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\9.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 164, 165  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\10.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 166, 167, 168, 169  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\11.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 170, 171, 172  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\12.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 173, 174, 175, 176 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2015\\13.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 177, 178, 179, 180  detalhadamente."}

pergunta2016_2 = {'Provas_do_ENEM\\ENEM\\2016\\1.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 136, 137, 138 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\2.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 139 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\3.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 140, 141, 142 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\4.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 143, 144, 145, 146 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\5.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 147, 148, 149 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\6.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 150, 151 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\7.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 152, 153, 154 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\8.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 155, 156, 157, 158 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\9.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 159, 160 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\10.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 161, 162, 163, 164 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\11.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 165, 166, 167 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\12.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 168, 169, 170, 171 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\13.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 172, 173, 174 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\14.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 175, 176, 177 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\15.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 178, 179, 180 e justifique cada escolha detalhadamente."}

pergunta2016_3 = {'Provas_do_ENEM\\ENEM\\2016\\1.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 136, 137, 138  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\2.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 139 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\3.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 140, 141, 142  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\4.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 143, 144, 145, 146  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\5.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 147, 148, 149  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\6.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 150, 151  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\7.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 152, 153, 154  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\8.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 155, 156, 157, 158  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\9.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 159, 160 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\10.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 161, 162, 163, 164  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\11.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 165, 166, 167  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\12.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 168, 169, 170, 171  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\13.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 172, 173, 174  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\14.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 175, 176, 177  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2016\\15.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 178, 179, 180  detalhadamente."}

pergunta2017_2 = {'Provas_do_ENEM\\ENEM\\2017\\1.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 136, 137, 138, 139 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\2.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 140, 141, 142, 143 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\3.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 144, 145, 146 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\4.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 147, 148 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\5.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 149, 150, 151, 152 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\6.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 153, 154, 155 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\7.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 156 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\8.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 157, 158, 159 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\9.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 160, 161, 162 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\10.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 163, 164, 165 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\11.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 166, 167, 168 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\12.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 169, 170, 171, 172 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\13.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 173 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\14.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 174, 175 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\15.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 176, 177 e justifique cada escolha detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\16.jpg': "Cada questão possui somente uma alternativa correta. Escolha a alternativa correta  para as questões 178, 179, 180 e justifique cada escolha detalhadamente."}

pergunta2017_3 = {'Provas_do_ENEM\\ENEM\\2017\\1.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 136, 137, 138, 139  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\2.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 140, 141, 142, 143 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\3.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 144, 145, 146  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\4.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 147, 148  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\5.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 149, 150, 151, 152  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\6.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 153, 154, 155  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\7.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 156  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\8.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 157, 158, 159  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\9.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 160, 161, 162 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\10.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 163, 164, 165  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\11.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 166, 167, 168 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\12.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 169, 170, 171, 172 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\13.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 173  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\14.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 174, 175 detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\15.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 176, 177  detalhadamente.",
                  'Provas_do_ENEM\\ENEM\\2017\\16.jpg': "Cada questão possui somente uma alternativa correta. Resolva as questões 178, 179, 180  detalhadamente."}


# Abrindo o arquivo
arquivo = open("ENEM_2015_Pergunta_3_ModeloProLatest_data_17_12_2024" + ".txt", "a", encoding="utf-8")
arquivo.write("ENEM 2015 Pergunta 3 Modelo ProLatest  data 17_12_2024 \n")
# Loop
for x in  ENEM_2015:
    # Escrevendo a imagem em que estamos trabalhando
    arquivo.write("\n" + x + "\n \n")
    # Escrevendo a pergunta em realação a essa imagem
    arquivo.write(pergunta2015_3[x] + "\n \n")
    # Uploud da imagem
    sample_file = genai.upload_file(path=x, display_name= x)
    # Resposta
    resposta = model2.generate_content([pergunta2015_3[x], sample_file])
    # Escrevendo a resposta
    arquivo.write(resposta.text)
# Fechando o arquivo
arquivo.close()
