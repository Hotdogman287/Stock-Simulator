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
price_list = [10, 5, 13, 9, 6, 10, 15, 21]
prices = len(price_list)
price_index = 0

#initial bar
x = 100
y = window_height/2


y_change = 0


pygame.draw.line(screen, grey, [x, y], [x+400, y])


#loop
running = True
while running:

        #drawing prices
        while price_index < prices:
            #draw to the screen
            if y_change >= 0:
                bar_color = red
            else:
                  bar_color = green



            pygame.draw.rect(screen, bar_color, [x, y, 20, y_change], 0) #this is drawing the first rectangle
            y_change = price_list[price_index]
            #y_change = price_list[price_index] - y_change
            #y = y - y_change
            x += 20
            print("Set price", price_index, "at", x, "change of", y)
            
            price_index += 1

        #end game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        #finishing steps per tick
        pygame.display.update() #updates screen

#end session (after the loop has ended)
pygame.quit()



