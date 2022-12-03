
def main( path ):

    rucksacks = [ list( line.strip() ) for line in open( path )  ]

    itemTypes = [ chr( n ) for n in range( ord( 'a' ), ord( 'z' ) + 1 ) ] + [ chr( n ) for n in range( ord( 'A' ), ord( 'Z' ) + 1 ) ]

    priorities = dict( zip( itemTypes, range( 1, 52 + 1 ) ) )

    errors = 0

    for rucksack in rucksacks:
        numOfItems = len( rucksack )
        comp1, comp2 = set( rucksack[ : ( numOfItems // 2 ) ] ), set( rucksack[ ( numOfItems // 2 ) : ] )
        errors += priorities[ ( comp1 & comp2 ).pop() ]

    return errors

assert ( main( "./Day3/test.txt" ) == 157 )

print( main( "./Day3/input.txt" ) )
