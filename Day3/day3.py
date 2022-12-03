
def main( path ):

    rucksacks = ( list( line.strip() ) for line in open( path )  )

    itemTypes = [ chr( n ) for n in range( ord( 'a' ), ord( 'z' ) + 1 ) ] + [ chr( n ) for n in range( ord( 'A' ), ord( 'Z' ) + 1 ) ]

    priorities = dict( zip( itemTypes, range( 1, 52 + 1 ) ) )

    errors = 0

    badges = 0

    for rucksack in rucksacks:

        group = [ rucksack, next( rucksacks ), next( rucksacks ) ]

        for elf in group:
            numOfItems = len( elf )
            comp1, comp2 = set( elf[ : ( numOfItems // 2 ) ] ), set( elf[ ( numOfItems // 2 ) : ] )
            errors += priorities[ ( comp1 & comp2 ).pop() ]

        rucksets = [ set( elf ) for elf in group ]
        badges += priorities[ ( rucksets[ 0 ] & rucksets[ 1 ] & rucksets[ 2 ] ).pop() ]

    return ( errors, badges )

assert ( main( "./Day3/test.txt" ) == ( 157, 70 ) )

print( main( "./Day3/input.txt" ) )
