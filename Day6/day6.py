def main( path ):

    answerPt1 = 0
    answerPt2 = 0

    with open( path ) as file:

        signal = file.read().rstrip()

        index = 0

        while( answerPt1 == 0 ):
            if( len( set( signal[ index : index + 4 : 1 ] ) ) == 4 ):
                answerPt1 = index + 4
            index += 1

        index = 0

        while( answerPt2 == 0 ):
            if( len( set( signal[ index : index + 14 : 1 ] ) ) == 14 ):
                answerPt2 = index + 14
            index += 1

    return ( answerPt1, answerPt2 )


testAnswers = [ ( 7, 19 ), ( 5, 23 ), ( 6, 23 ), ( 10, 29 ), ( 11, 26 ) ]

for i in range( len( testAnswers ) ):
    assert ( main( "./Day6/test" + str( i ) + ".txt" ) == testAnswers[ i ] )

print( main( "./Day6/input.txt" ) )
