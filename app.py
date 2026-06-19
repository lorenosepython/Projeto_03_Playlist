import streamlit as st

musicas = {
    "Melanie Martinez": {
        "Lunchbox friends": "https://www.youtube.com/watch?v=2khRy7zAKyQ&pp=ygURbHVuY2ggYm94IGZyaWVuZHM%3D",
        "High School Sweethearts": "https://www.youtube.com/watch?v=TkOHVGNw7EY&pp=ygUXaGlnaCBzY2hvb2wgc3dlZXRoZWFydHM%3D",
    },
    "Tyler the creator": {
        "EARFQUAKE": "https://www.youtube.com/watch?v=Aztdmq1tYY8&pp=ygUJZWFyZnF1YWtl",
        "I THINK": "https://www.youtube.com/watch?v=juON1q58tWE&pp=ygUHaSB0aGluaw%3D%3D",
    },
    "Deftones": {
        "Mascara": "https://www.youtube.com/watch?v=mfBRKxQZ4Ng&pp=ygUQbWFzY2FyYSBkZWZ0b25lc9IHCQk-CwGHKiGM7w%3D%3D",
        'Entombed': 'https://www.youtube.com/watch?v=67oBykAKUuk&pp=ygURZW50b21iZWQgZGVmdG9uZXM%3D'
}


}
st.sidebar.image('logo.png')
artista = st.sidebar.selectbox('selecione o artista', musicas.keys())
musicas_artista = musicas[artista]
video,sobre = st.tabs(['video','sobre'])

st.title(artista)
with video:
    for musica in musicas_artista.items():
        titulo, link = musica
        st.subheader(titulo)
    st.video(link)
    


with sobre:
    if artista == 'Melanie Martinez':
        st.markdown('__Quem é Melanie Martinez?:__ Melanie Martinez é uma cantora, compositora, diretora e artista visual norte-americana que ganhou destaque em 2012 ao participar do programa The Voice. Mesmo não vencendo a competição, ela chamou atenção por sua voz única e seu estilo criativo. Em 2015 lançou seu primeiro álbum, Cry Baby, que rapidamente conquistou fãs ao redor do mundo. O álbum conta a história de uma personagem fictícia chamada Cry Baby, usada por Melanie para abordar temas como insegurança, bullying, relacionamentos, traumas da infância e saúde mental. Além da música, Melanie é conhecida por criar universos visuais completos para seus projetos, produzindo videoclipes e filmes que complementam suas histórias. Em 2019 lançou o álbum K-12, acompanhado de um filme musical dirigido por ela mesma. Já em 2023 apresentou Portals, um projeto que marcou uma nova fase artística, explorando temas como transformação, renascimento e crescimento pessoal. Sua estética diferenciada, combinando elementos infantis com mensagens profundas, fez dela uma das artistas mais originais do pop alternativo atual.')
    elif artista == 'Tyler the creator':
        st.markdown('__Quem é Tyler the creator?:__ Tyler, The Creator é um rapper, produtor musical, compositor, diretor e empresário norte-americano considerado um dos artistas mais influentes da música contemporânea. Nascido em 1991 na Califórnia, ele começou sua carreira como líder do coletivo de hip-hop Odd Future, que ganhou popularidade na internet por seu estilo irreverente e inovador. Tyler ficou conhecido por produzir suas próprias músicas e por desenvolver uma identidade artística única, misturando rap, jazz, soul, funk e R&B. Ao longo de sua carreira lançou álbuns de grande sucesso como Goblin, Wolf, Flower Boy, IGOR e Call Me If You Get Lost. O álbum IGOR venceu o Grammy de Melhor Álbum de Rap e é considerado uma de suas obras mais importantes. Além da música, Tyler também se destaca no mundo da moda com as marcas Golf Wang e Golf le Fleur, além de ser criador do festival Camp Flog Gnaw. Sua criatividade, autenticidade e constante evolução artística fizeram dele uma referência para uma nova geração de músicos e fãs.')
    elif artista == 'Deftones':
        st.markdown('__Quem são Deftones?:__ Deftones é uma banda norte-americana formada em 1988 na cidade de Sacramento, Califórnia. O grupo é composto principalmente por Chino Moreno, Stephen Carpenter, Abe Cunningham e Frank Delgado. Conhecida por misturar metal alternativo, rock experimental, shoegaze e nu metal, a banda desenvolveu um som único que combina guitarras pesadas, atmosferas melancólicas e vocais emocionais. O álbum White Pony, lançado em 2000, é considerado um dos trabalhos mais influentes da história do metal alternativo e ajudou a consolidar a reputação da banda mundialmente. Outros álbuns importantes incluem Around the Fur, Diamond Eyes, Koi No Yokan e Ohms. Ao longo de mais de três décadas de carreira, os Deftones conquistaram uma base de fãs extremamente fiel e influenciaram diversas bandas de rock e metal. Seu diferencial está na capacidade de unir agressividade sonora com melodias suaves e ambientes sonhadores, criando uma identidade musical que permanece relevante até os dias atuais.')
