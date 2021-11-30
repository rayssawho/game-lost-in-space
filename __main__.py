import pygame
from pygame.locals import *
from sys import exit
import os
import random

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'images')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

pygame.init()
pygame.mixer.init()

largura = 1366
altura = 768

fundotela = (255, 255, 255)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Lost in Space")


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprites2.png')).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'smw_lemmy_wendy_incorrect.wav'))
som_colisao.set_volume(1)

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'smw_coin.wav'))
som_pontuacao.set_volume(1)

som_jogo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'mathgrant.wav'))
som_jogo.set_volume(1)

colidiu = False

escolha_obstaculo = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

pontos = 0

velocidade_jogo = 20

def exibe_mensagem(msg, tamanho, cor):
    
    fonte = pygame.font.SysFont('Impact', tamanho, False, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global pontos, velocidade_jogo, colidiu, escolha_obstaculo
    pontos = 0
    velocidade_jogo = 20
    colidiu = False
    astro.rect.y = 430 - 434//2
    astro.pulo = False
    
    
    nave1.rect.x = largura
    nave2.rect.x = largura
    nave3.rect.x = largura
    nave4.rect.x = largura
    pedra1.rect.x = largura
    planeta1.rect.x = largura
    planeta2.rect.x = largura
    planeta3.rect.x = largura
    planeta4.rect.x = largura
    planeta5.rect.x = largura
    planeta6.rect.x = largura
    planeta7.rect.x = largura
    planeta8.rect.x = largura
    planeta9.rect.x = largura
    foguete1.rect.x = largura
    escolha_obstaculo = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        
    

class Astronauta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'smw_spin_jump.wav'))
        self.som_pulo.set_volume(1)
        self.image = sprite_sheet.subsurface((0*2606, 0), (2606, 2605))
        self.image = pygame.transform.scale(self.image, (360, 361))
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = 500 - 200//2
        self.rect.center = (300, 60)
        self.pulo = False    
    
    def pular(self):
        self.pulo = True
        self.som_pulo.play()
              
    
    def update(self):
        if self.pulo == True:
            if self.rect.y <= 10:
                self.pulo = False
            self.rect.y -= 10
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 10
            else:
                self.rect.y = self.pos_y_inicial
            
        
 

class Nave1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*2606, 0), (2606, 2605))
        self.image = pygame.transform.scale(self.image, (500, 501))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 100)
        self.rect.x = largura
    
    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo

class Pedra1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1100, 1101))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 580) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo
            
class Planeta1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1290, 1291))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 600) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 2:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo
        
class Planeta2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1200, 1201))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 40) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 3:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo   

class Planeta3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1300, 1301))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 680) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 4:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo      


class Planeta4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1000, 1001))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 50) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 5:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo      

class Planeta5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1350, 1351))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 20) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 6:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo          

class Planeta6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((8*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1200, 1201))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 650) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 7:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo          
            
class Planeta7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((9*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1400, 1401))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 50) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 8:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo          

class Planeta8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((10*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1000, 1001))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 650) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 9:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
            
class Planeta9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((11*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (1350, 1351))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 580) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 10:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
        

class Nave2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((12*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (750, 751))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 100) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 11:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
        
        
class Foguete(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((13*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (800, 801))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 600) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 12:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
            
class Nave3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((14*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (700, 701))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 550) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 13:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
            
class Nave4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((15*2606, 0), (2606,2605))
        self.image = pygame.transform.scale(self.image, (700, 701))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, 100) 
        self.rect.x = largura  
        
    def update(self):
        if self.escolha == 14:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo  
        

todas_as_sprites = pygame.sprite.Group()

astro = Astronauta()
todas_as_sprites.add(astro)

nave1 = Nave1()
todas_as_sprites.add(nave1)

nave2 = Nave2()
todas_as_sprites.add(nave2)

nave3 = Nave3()
todas_as_sprites.add(nave3)

nave4 = Nave4()
todas_as_sprites.add(nave4)

pedra1 = Pedra1()
todas_as_sprites.add(pedra1)

planeta1 = Planeta1()
todas_as_sprites.add(planeta1)

planeta2 = Planeta2()
todas_as_sprites.add(planeta2)

planeta3 = Planeta3()
todas_as_sprites.add(planeta3)

planeta4 = Planeta4()
todas_as_sprites.add(planeta4)

planeta5 = Planeta5()
todas_as_sprites.add(planeta5)

planeta6 = Planeta6()
todas_as_sprites.add(planeta6)

planeta7 = Planeta7()
todas_as_sprites.add(planeta7)

planeta8 = Planeta8()
todas_as_sprites.add(planeta8)

planeta9 = Planeta9()
todas_as_sprites.add(planeta9)

foguete1 = Foguete()
todas_as_sprites.add(foguete1)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(nave1)
grupo_obstaculos.add(nave2)
grupo_obstaculos.add(nave3)
grupo_obstaculos.add(nave4)
grupo_obstaculos.add(pedra1)
grupo_obstaculos.add(planeta1)
grupo_obstaculos.add(planeta2)
grupo_obstaculos.add(planeta3)
grupo_obstaculos.add(planeta4)
grupo_obstaculos.add(planeta5)
grupo_obstaculos.add(planeta6)
grupo_obstaculos.add(planeta7)
grupo_obstaculos.add(planeta8)
grupo_obstaculos.add(planeta9)
grupo_obstaculos.add(foguete1)



imagem_bg = pygame.image.load(os.path.join(diretorio_imagens, 'bg2.jpg')).convert()
imagem_bg = pygame.transform.scale(imagem_bg, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(35)
    tela.fill(fundotela)
    
    for event in pygame.event.get():
        som_jogo.play()
        if event.type == QUIT:
            pygame.quit()
            exit()
            som_jogo.stop()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and colidiu == False:
                
                if astro.rect.y != astro.pos_y_inicial:
                    pass   
                astro.pular()
            if event.key == K_r and colidiu == True:
                
                reiniciar_jogo()
    
    colisoes = pygame.sprite.spritecollide(astro, grupo_obstaculos, False, pygame.sprite.collide_mask)
    
    tela.blit(imagem_bg, (0,0))
    todas_as_sprites.draw(tela)
    
    
    if (nave1.rect.topright[0] <= 0 or nave2.rect.topright[0] <= 0 or nave3.rect.topright[0] <= 0 
        or nave4.rect.topright[0] <= 0 or pedra1.rect.topright[0] <= 0 or planeta1.rect.topright[0] <= 0 or 
        planeta2.rect.topright[0] <= 0 or planeta3.rect.topright[0] <= 0 or planeta4.rect.topright[0] <= 0 or
        planeta5.rect.topright[0] <= 0 or planeta6.rect.topright[0] <= 0 or planeta7.rect.topright[0] <= 0 or
        planeta8.rect.topright[0] <= 0 or planeta9.rect.topright[0] <= 0 or foguete1.rect.topright[0] <= 0):
    
        escolha_obstaculo = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        nave1.rect.x = largura
        nave2.rect.x = largura
        nave3.rect.x = largura
        nave4.rect.x = largura
        pedra1.rect.x = largura
        planeta1.rect.x = largura
        planeta2.rect.x = largura
        planeta3.rect.x = largura
        planeta4.rect.x = largura
        planeta5.rect.x = largura
        planeta6.rect.x = largura
        planeta7.rect.x = largura
        planeta8.rect.x = largura
        planeta9.rect.x = largura
        foguete1.rect.x = largura
        nave1.escolha = escolha_obstaculo
        nave2.escolha = escolha_obstaculo
        nave3.escolha = escolha_obstaculo
        nave4.escolha = escolha_obstaculo
        pedra1.escolha = escolha_obstaculo
        planeta1.escolha = escolha_obstaculo
        planeta2.escolha = escolha_obstaculo
        planeta3.escolha = escolha_obstaculo
        planeta4.escolha = escolha_obstaculo
        planeta5.escolha = escolha_obstaculo
        planeta6.escolha = escolha_obstaculo
        planeta7.escolha = escolha_obstaculo
        planeta8.escolha = escolha_obstaculo
        planeta9.escolha = escolha_obstaculo
        foguete1.escolha = escolha_obstaculo
        
    
    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True
    
      
        
    if colidiu == True:
        
        if pontos % 100 == 0:
            pontos += 1
        
        perdeu = exibe_mensagem('GAME OVER', 98, (255, 255, 255))
        tela.blit(perdeu, (largura//2, altura//2))
        restart = exibe_mensagem('Pressione R para Reiniciar', 40, (255, 255, 255))
        tela.blit(restart, (largura//2, (altura//2) + 110))
        
    else:
        pontos += 1
        todas_as_sprites.update()
        texto_pontos = exibe_mensagem(pontos, 60, (255, 255, 255))
    
    if pontos % 100 == 0:
        som_pontuacao.play()
        
        if velocidade_jogo >= 100:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 3
            
            
    
    tela.blit(texto_pontos, (1150, 70))    
      
    pygame.display.update()    
    pygame.display.flip()
