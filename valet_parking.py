#-------------------------------------------------------
# Part 1
#-------------------------------------------------------

#determines whether there is room in the parking lane and whether it is empty.
def empty_or_full(parking_lane, capacity): 
    # The body of your function goes here
    if len(parking_lane) == 0:
        return 'empty'
    elif len(parking_lane) == capacity:
        return 'full'
    else:
        return 'neither'
'''print(empty_or_full([1, 2, 3], 3)) #full
print(empty_or_full([1, 2, 3], 10)) #neither
print(empty_or_full([], 1)) #empty'''


#move cars from str list cars_to_park to str list parking_lane up to capacity
#process: for i in cars_to_park: move = cars.pop(i), parking_lane.append(move)
#return str(parking_lane)
def park_cars(parking_lane, capacity, cars_to_park):
    # The body of your function goes here
    for i in cars_to_park:
        if len(parking_lane) < capacity:
            move = cars_to_park[cars_to_park.index(i)]
            parking_lane.append(move)
    return parking_lane

#post: removes parking_lane[] cars listed in cars_to_retrieve[]
#return str version of parking_lane after changes
#traverse through cars_to_retrieve. if car in parking_lane,
#                                  parking_lane.remove(car)
def retrieve_cars(parking_lane, cars_to_retrieve):
    # The body of your function goes here
    for car in cars_to_retrieve:
        if car in parking_lane:
            parking_lane.remove(car)
    return parking_lane
#print(retrieve_cars(['FF 22', 'LKJ-7250'], ['RTY-5655']))

#verifies all of the cars in cars_to_check are in parking_lane.
#True if all of the cars in cars_to_check are in parking_lane, else False
#for car in cars_to_check: if car not in parking_lane: return False. 
#return True at end
def check_cars(parking_lane, cars_to_check):
    # The body of your function goes here
    for car in cars_to_check:
        if car not in parking_lane:
            return False
    return True
'''print(check_cars(['RTY-5655'], ['FF 22', 'LKJ-7250'])) #→ False
print(check_cars(['FF 22', 'LKJ-7250'], ['RTY-5655'])) #→ False
print(check_cars(['FF 22', 'LKJ-7250'], ['FF 22'])) #→ True
print(check_cars(['RTY-5655'], [])) #→ True'''

#-------------------------------------------------------
# Part 2
#-------------------------------------------------------
#Return which list bubble is in
def bubble_list(parking_lane, service_lane):
    if '' in parking_lane:
        return parking_lane
    else:
        return service_lane

#Return which list bubble isn't in
def other_list(parking_lane, service_lane):
    if '' in parking_lane:
            return service_lane
    else:
        return parking_lane

#Pre: car str, parking_lane, service_lane
#Post: return index of car 
def car_index(car_lane, car):
    return car_lane.index(car)

#print(car_index([1,2,3], [4, 5, 6], 5)) # 1

#Pre: parking_lane, service_lane
#Post: return index of bubble (if statements to test each lane)
def bubble_index(bubble_lane):
    return bubble_lane.index('')
    
#print(bubble_index([1,2,''], [4, 5, 6])) # 2   


#Pre: parking_lane (str list), service_lane (str list), bubble_moves (str list)
#get index of bubble, store value at same index in other list in temp, 
    #put bubble into same index of other list, put temp into same index of 
    #other list
    #append O to bubble_moves (void, returns nothing)
def swap_lanes(parking_lane, service_lane, bubble_lane, bubble_moves):
    bub_index = bubble_index(bubble_lane)
    other_lane = other_list(parking_lane, service_lane)
    #swap bubble with car in other lane
    other_car = other_lane[bub_index]
    other_lane[bub_index] = ''
    bubble_lane[bub_index] = other_car
        
    bubble_moves.append('O')
    #return parking_lane, service_lane, bubble_moves
#print(swap_lanes([1,2,''], [1,2,3],[])) #([1, 2, 3], [1, 2, ''], ['O'])

#Pre: parking_lane (str list), service_lane (str list), bubble_moves (str list)
#L: get index of bubble, store value at previous index in temp, put bubble into 
    #previous index, put temp in current index
    #bubble_moves.append('L')
def up_lane(bubble_lane, bubble_moves): 
#might require just one bubble list if you have to find it in main anyway
    bub_index = bubble_index(bubble_lane)
    
    #swap bubble with car of lower index
    temp = bubble_lane[bub_index-1]
    bubble_lane[bub_index-1] = ''
    bubble_lane[bub_index] = temp
    
    bubble_moves.append('L')
    #return bubble_lane, bubble_moves    
#print(up_lane([1,2,3],[1,2,''],['O']))    # [1,'',2], ['O','L']

#Pre: parking_lane (str list), service_lane (str list), bubble_moves (str list)
#Post: H: get index of bubble + 1, store value at next index in temp, put bubble
     #into next index, put temp in previous index
    #bubble_moves.append('H')
def down_lane(bubble_lane, bubble_moves):
    bub_index = bubble_index(bubble_lane)
    
    if bub_index != len(bubble_lane)-1: #if bubble isn't at last index
        next_index = bub_index + 1
        temp = bubble_lane[next_index]
        bubble_lane[next_index] = ''
        bubble_lane[bub_index] = temp
        bubble_moves.append('H')
    #return bubble_lane, bubble_moves 
'''print(down_lane([1,2,''],[3,4,5],[]))   #[1,2,''], ['H']
print(down_lane([1,2,3],['',4,5],[]))   #[4,'',5], ['H']'''

    
'''
    #if car_index == 0, return []

    #while car_index > 1, move car to index 1 and bubble to index 0
        Generally keep bubble one above car
        #If bubble is more than one above car, then H until one above. (while)
        
        > Move car up the lane until it is at index 1
            > By always keeping bubble one above car and switching 
            > If more than one move up is required for car, 
            then always keep bubble above car (below), then switch
            > Switch at end   
    '''  
#parking_lane = str list, service_lane = str list, car = str
#return a list[str] of movement codes it took to bring bubble to index 0 of same
# lane
#Codes: O = shift bubble to Other lane, 
#L = shift bubble to Lower index, H = shift bubble to Higher index
def swap_to_front(parking_lane, service_lane, car):
    # The body of your function goes here
      
    #BUBBLE MUST GO INTO PREVIOUS INDEX (INDEX 0) TO SWAP WITH CAR
    #The goal: move bubble to index 0 of list where car is and car up to index 1  
    bubble_moves = []
    
    if car in parking_lane:
        car_lane = parking_lane
    else:
        car_lane = service_lane
        
    bubble_lane = bubble_list(parking_lane,service_lane)
    
    if car_index(car_lane,car) == 0:
        return []
    
    #Brings bubble up to index 0 and car up to index 1 of same list, 
    #then swaps to bring car to front
    while car_index(car_lane,car) >= 1:      
        #ALWAYS KEEP BUBBLE ONE SPACE ABOVE CAR
        #if bubble is at same index as car
        if bubble_index(bubble_lane) == car_index(car_lane,car):
            up_lane(bubble_lane,bubble_moves)
            swap_lanes(parking_lane,service_lane,bubble_lane,bubble_moves)
            bubble_lane = bubble_list(parking_lane,service_lane)
        
        #if bubble is at least one above:
        elif bubble_index(bubble_lane) < car_index(car_lane,car):
            if '' not in car_lane: #swap lanes
                swap_lanes(parking_lane,service_lane,bubble_lane,bubble_moves)
                bubble_lane = bubble_list(parking_lane,service_lane)
            bubble_i = bubble_index(bubble_lane)
            for i in range(bubble_i,car_index(car_lane,car)):
                down_lane(bubble_lane,bubble_moves)
        
        #if bubble is at least one below: 
        elif bubble_index(bubble_lane) > car_index(car_lane,car):
            #if bubble in car_lane
            if '' in car_lane: #swap lanes
                swap_lanes(parking_lane,service_lane,bubble_lane,bubble_moves) 
                bubble_lane = bubble_list(parking_lane,service_lane)
            #move bubble up (L, 1 less than car index)
            bubble_i = bubble_index(bubble_lane)
            for i in range(bubble_i, car_index(car_lane,car)-1,-1):
                up_lane(bubble_lane,bubble_moves)
            #swap lanes to go 1 above car
            swap_lanes(parking_lane,service_lane,bubble_lane,bubble_moves)
            bubble_lane = bubble_list(parking_lane,service_lane)
        
        if car_index(car_lane,car) == 0:
            break
        #Move car up until it's at index 0
        down_lane(bubble_lane,bubble_moves)
    return bubble_moves
'''print(swap_to_front(['', 'N00B-DRV', 'ONT123'], 'LKJ-7250')) #OH
print(swap_to_front(['N00B-DRV', '', 'ONT123'], 'LKJ-7250')) #LOH
print(swap_to_front(['N00B-DRV', '', 'ONT123'], 'FF 22')) #[]
'''

    
        
        
        
    

    
    
    
    

    
    
    
    




