import pygame
import random


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

price_change = []
gen = True
num = 0
num_gend = 0
num_gen = int(input("how many prices should be generated?"))
while gen:
    num = random.randint(-20, 20)
    price_change.append(num)
    num_gend += 1
    if num_gend >= num_gen:
        gen = False

price_change.append(0)
price_change.append(3)

#price_change = [10, 5, -13, 9, 6, 10, -15, 21, -4, -10, 5, -20, -40, 21]
prices = [0] #will be generated later


starting_price = 0
generating_price_list = True
price_generation_step = 0

#generate total prices list
while generating_price_list:
        prices.append(prices[price_generation_step] + price_change[price_generation_step])
        price_generation_step += 1
        if len(prices) >= len(price_change):
               generating_price_list = False
               print(prices)




drawn = 0
prices_number = len(price_change)
price_index = 0



change = 0


#resizing bars
peak = max(prices)
print(peak)
trough = min(prices)
print(trough)
x = 100
graph_amplification = (window_height-200)/(peak - trough)
print("graph amplification:", graph_amplification)
y = 100 + (peak * graph_amplification)
print("starting height", y)
pygame.draw.line(screen, grey, [x-20, y], [x+400, y])

#loop
running = True
while running:

        


        #drawing prices_number
        while price_index < prices_number:
            change = graph_amplification*price_change[price_index]
            #draw to the screen
            if change > 0:
                bar_color = green
                pygame.draw.rect(screen, bar_color, [x, y - change, 20, change], 0) #this is drawing the first rectangle
            elif change < 0:
                bar_color = red
                pygame.draw.rect(screen, bar_color, [x, y, 20, -change], 0) #this is drawing the first rectangle
            else:
                pygame.draw.line(screen, grey, [x, y], [x+20, y])

            y = y - change
            x += 20
            #print("PriceID:", price_index, "Change:", change)
            
            price_index += 1

        #end game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        #finishing steps per tick
        pygame.display.update() #updates screen

#end session (after the loop has ended)
pygame.quit()



