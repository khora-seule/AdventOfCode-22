
def main( path ):

    transOpp  = dict( zip( [ "A", "B", "C" ], range( 3 ) ) )
    transSelf = dict( zip( [ "X", "Y", "Z" ], range( 3 ) ) )

    guide = [ line.split() for line in open( path )  ]
    naiveScores = []
    actualScores = []

    for round in guide:

        opp, self = transOpp[ round[ 0 ] ], transSelf[ round[ 1 ] ]

        naiveScore = ( 1 + self ) + 3 * range(3)[ ( self - opp + 1 ) % 3 ]
        actualScore = ( 1 + range(3)[ ( self + opp - 1 ) % 3 ] ) + 3 * self
        
        naiveScores = naiveScores + [ naiveScore ]
        actualScores = actualScores + [ actualScore ]

    part1 = sum( naiveScores )
    part2 = sum( actualScores )

    return ( part1, part2 )


assert ( main( "./Day2/test.txt" ) == ( 15, 12 ) )

print( main( "./Day2/input.txt" ) )