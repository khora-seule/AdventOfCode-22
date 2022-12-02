
def main( path ):

    inventory = []

    with open( path ) as file:
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
    part1 = ( totalsSorted[ 0 ][ 0 ] )

    # Part 2
    part2 = sum ( [ elf[ 0 ] for elf in totalsSorted[ :3 ] ] )

    return ( part1, part2 )

assert ( main( "./Day1/test.txt" ) == ( 24000, 45000 ) )

print( main( "./Day1/input.txt" ) )