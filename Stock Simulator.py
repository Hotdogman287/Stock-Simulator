import pygame



#starting variables
window_width = 800
window_height = 450


#colors
red = (255, 0, 0)
green = (0, 255, 0)





#window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Stock Market Sim")

price_change = .2
drawn = 0
price_list = {100, 110, 130, 90}
prices = len(price_list)
drawn_prices = 0


#loop
running = True
while running:

        while drawn_prices < prices:
            #draw to the screen
            pygame.draw.rect(screen, red, [100, 100, 400, 100], 0) #this is drawing the first rectangle
            drawn_prices += 1
        

        #end game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        #finishing steps per tick
        pygame.display.update() #updates screen

#end session (after the loop has ended)
pygame.quit()



