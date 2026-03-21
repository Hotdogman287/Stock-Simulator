import pygame
import random


#starting variables
window_width = 800
window_height = 450

#colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grey = (50, 50, 50)




#window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Stock Market Sim")
pygame.draw.rect(screen, grey, [0, 0 , 60, window_height], 0)
pygame.draw.rect(screen, grey, [60, 0 , window_width-60, 60], 0)
pygame.draw.rect(screen, grey, [60, window_height-60 , window_width-60, 60], 0)

#GENERATE RANDOM MARKET
price_change = []
gen = True
num = 0
num_gend = 0
#num_gen = int(input("how many prices should be generated?"))
num_gen = 23
while gen:
    num = random.randint(-10, 10)
    price_change.append(num)
    num_gend += 1
    if num_gend >= num_gen:
        gen = False

price_change.append(0)
price_change.append(3)

print("The Price Change is:", price_change)




base_price = 100
price_change = [1, -1, -1, 1, 2, -1, -2, 1, 1, -1, -1, 1]
prices = [base_price] #will be generated later



generating_price_list = True
price_generation_step = 0

#generate total prices list
while generating_price_list:
        prices.append(prices[price_generation_step] + price_change[price_generation_step])
        price_generation_step += 1
        if len(prices) >= len(price_change):
               generating_price_list = False
               print("Total Prices", prices)






#resizing bars
peak = max(prices)
peak_dif = peak - base_price
print("Peak:", peak)

trough = min(prices)
trough_dif = trough - base_price
print("Trough:", trough)

range = peak - trough

x = 100
graph_amplification = (window_height-200)/(peak - trough)

print("graph amplification:", graph_amplification)

#WORK ON THIS
y = 100 + (range - peak_dif)*graph_amplification+window_height -350

print("starting height", y)
pygame.draw.line(screen, white, [x-20, y], [window_width-x, y], 3)

#loop
drawn = 0
prices_number = len(price_change)
price_index = 0
change = 0
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
                pygame.draw.line(screen, white, [x, y], [x+20, y])

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



