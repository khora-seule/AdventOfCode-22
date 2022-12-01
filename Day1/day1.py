
inventory = []

with open( "./Day1/input.txt" ) as file:
    pers = []
    index = 0
    for line in file:
        
        match line:
            case "\n":
                inventory = inventory + [ ( pers, index ) ]
                index = index + 1
                pers = []
            case other:
                pers += [ int( line.strip() ) ]

totals = [ ( sum( elf[ 0 ] ), elf[ 1 ] ) for elf in inventory ]

totalsSorted = sorted( totals, key = lambda elf : elf[ 0 ], reverse = True )

# Part 1
print ( totalsSorted[ 0 ] )

# Part 2
print( sum ( [ elf[ 0 ] for elf in totalsSorted[ :3 ] ] ) )
