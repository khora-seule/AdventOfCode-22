
def main( path ):

    pairAssignments = [ [ [ int( assignment ) for assignment in assignments.strip().split( "-" ) ] for assignments in line.split( "," ) ] for line in open( path ) ]

    totalOverlaps = 0
    overlaps = 0

    for pair in pairAssignments:
        
        firstPair = set( range( pair[ 0 ][ 0 ], pair[ 0 ][ 1 ] + 1 ) )
        secondPair = set( range( pair[ 1 ][ 0 ], pair[ 1 ][ 1 ] + 1) )
        overlap = firstPair & secondPair

        if( overlap in [ firstPair, secondPair ] ):
            totalOverlaps += 1

        if( overlap != set() ):
            overlaps += 1

    return ( totalOverlaps, overlaps )

assert ( main( "./Day4/test.txt" ) == ( 2, 4 ) )

print( main( "./Day4/input.txt" ) )
