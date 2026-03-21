import pygame



#starting variables
window_width = 800
window_height = 450


#colors
red = (255, 0, 0)
green = (0, 255, 0)
grey = (30, 30, 30)




#window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Stock Market Sim")

price_change = .2
drawn = 0
price_change = [10, 5, -13, 9, 6, 10, -15, 21, -4, -10, 5, -20]
prices = len(price_change)
price_index = 0

#initial bar
x = 100
y = window_height/2


change = 0


pygame.draw.line(screen, grey, [x, y], [x+400, y])


#loop
running = True
while running:

        #drawing prices
        while price_index < prices:
            change = price_change[price_index]
            #draw to the screen
            if change >= 0:
                bar_color = green
                pygame.draw.rect(screen, bar_color, [x, y - change, 20, change], 0) #this is drawing the first rectangle
            else:
                bar_color = red
                pygame.draw.rect(screen, bar_color, [x, y, 20, -change], 0) #this is drawing the first rectangle

            y = y - change
            x += 20
            print("PriceID:", price_index, "Change:", change)
            
            price_index += 1

        #end game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        #finishing steps per tick
        pygame.display.update() #updates screen

#end session (after the loop has ended)
pygame.quit()



