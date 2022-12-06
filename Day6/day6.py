def main( path ):

    return


testAnswers = [ 7, 5, 6, 10, 11 ]

for i in range( len( testAnswers ) ):
    assert ( main( "./Day6/test" + str( i ) + ".txt" ) == testAnswers[ i ] )

print( main( "./Day6/input.txt" ) )
