#!/usr/bin/python3.6

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Historia de um garoto e seus brinquedos.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

matrix = media.Movie("Matrix",
                     "O mundo esta tomado por maquinas e todos estao conectados a um mundo virtual",
                     "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
#print(matrix.storyline)

os_incriveis = media.Movie("Os Incriveis",
                           "Depois que o governo baniu o uso de superpoderes, o maior heroi do planeta, o Sr. Incrivel, vive agora uma vida normal e pacata com sua familia.",
                           "https://upload.wikimedia.org/wikipedia/pt/4/4b/Os_Incr%C3%ADveis.jpg",
                           "https://www.youtube.com/watch?v=uz5nMVBGDjk")

prometheus = media.Movie("Prometheus",
                        "Este preludio do filme Alien conta a historia de uma equipe de cientistas que embarca em uma jornada espacial para descobrir a verdade sobre a origem da raca humana.",
                        "https://upload.wikimedia.org/wikipedia/pt/b/b8/Prometheus-P%C3%B4ster.jpg",
                        "https://www.youtube.com/watch?v=sftuxbvGwiU")
#prometheus.show_trailer()

velozes_e_furiosos = media.Movie("Velozes e Furiosos",
                                 "Brian O'Conner e um policial que se infiltra no submundo dos rachas de rua para investigar uma serie de furtos.",
                                 "https://upload.wikimedia.org/wikipedia/pt/f/f9/TheFastandtheFurious.jpg",
                                 "https://www.youtube.com/watch?v=erKtbT8A_Eg")

star_trek = media.Movie("Star Trek",
                        "A bordo do USS Enterprise, a nave mais sofisticada ja construida, uma tripulacao de novatos embarca em sua viagem inaugural, que e atrapalhada por Nero, um comandante cuja vinganca ameaca toda a humanidade.",
                        "https://upload.wikimedia.org/wikipedia/pt/c/c9/StarTrek11.jpg",
                        "https://www.youtube.com/watch?v=G2_tdI-cZBA")

guardioes_da_galaxia = media.Movie("Guardioes da Galaxia",
                                   "O aventureiro do espaço Peter Quill torna-se presa de cacadores de recompensas depois que rouba a esfera de um vilao traicoeiro, Ronan.",
                                   "https://upload.wikimedia.org/wikipedia/pt/b/b2/Guardiansgalaxyposter.jpg",
                                   "https://www.youtube.com/watch?v=8VN_l57QWyQ")

mulher_maravilha = media.Movie("Mulher Maravilha",
                               "Treinada desde cedo para ser uma guerreira imbativel, Diana Prince nunca saiu da paradisiaca ilha em que e reconhecida como princesa das Amazonas.",
                               "https://upload.wikimedia.org/wikipedia/pt/f/fc/P%C3%B4ster_Wonder_Woman.jpg",
                               "https://www.youtube.com/watch?v=I6Gj8Fvukk4")

homem_de_ferro = media.Movie("Homem de Ferro",
                             "Tony Stark e um industrial bilionario e inventor brilhante que realiza testes belicos no exterior, mas e sequestrado por terroristas que o forcam a construir uma arma devastadora.",
                             "https://upload.wikimedia.org/wikipedia/pt/0/00/Iron_Man_poster.jpg",
                             "https://www.youtube.com/watch?v=xXAdp_KJ-0A")

capitao_america = media.Movie("Capitao America",
                              "Steve Rogers e um jovem que participa de experiencias visando a criacao do supersoldado americano.",
                              "https://upload.wikimedia.org/wikipedia/pt/d/d8/Capit%C3%A3o_Am%C3%A9rica_O_Primeiro_Vingador_-_Poster.jpg",
                              "https://www.youtube.com/watch?v=3p1d_6_ocEE")

movies = [toy_story, matrix, os_incriveis, prometheus, velozes_e_furiosos, star_trek, guardioes_da_galaxia, mulher_maravilha, homem_de_ferro, capitao_america]
fresh_tomatoes.open_movies_page(movies)


