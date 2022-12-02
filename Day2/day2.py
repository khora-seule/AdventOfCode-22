
def main( path ):

    transOpp  = dict( zip( [ "A", "B", "C" ], range( 3 ) ) )
    transSelf = dict( zip( [ "X", "Y", "Z" ], range( 3 ) ) )

    guide = [ line.split() for line in open( path )  ]
    scores = []

    for round in guide:

        opp, self = transOpp[ round[ 0 ] ], transSelf[ round[ 1 ] ]

        score = ( 1 + self ) + 3 * range(3)[ ( self - opp + 1 ) % 3 ]
        
        scores = scores + [ score ]
    
    return sum( scores )


assert ( main( "./Day2/test.txt" ) == 15 )

print( main( "./Day2/input.txt" ) )