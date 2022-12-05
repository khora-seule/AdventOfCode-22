
def main( path ):

    crateStackRows = []
    moves = []
    current = "crates"

    with open( path ) as file:
        for line in file:

            match line:
                case "\n":
                    current = "moves"

                case other:

                    if current == "crates":
                        crateStackRows += [ list( line )[ 1 : : 4 ] ]

                    if current == "moves":
                        moves += [ [ int( value ) - 1 for value in line.split()[ 1 : : 2 ] ] ]
                    
    crateStacks = [ [ row[ int( index ) - 1 ] for row in crateStackRows[ : -1 ] if row[ int( index ) - 1 ] != ' ' ] for index in crateStackRows[ - 1 ] ]

    pivot = ( [ value for value in crateStacks ], [ value for value in crateStacks ] )

    for ( quantity, first, second ) in moves:
        
        pivot[ 0 ][ second ] = pivot[ 0 ][ first ][ quantity :  : -1 ] + pivot[ 0 ][ second ]
        pivot[ 0 ][ first ] = pivot[ 0 ][ first ][ quantity + 1 : ]
    
    for ( quantity, first, second ) in moves:
        
        pivot[ 1 ][ second ] = pivot[ 1 ][ first ][ : quantity + 1 ] + pivot[ 1 ][ second ]
        pivot[ 1 ][ first ] = pivot[ 1 ][ first ][ quantity + 1 : ]
    
    tops9000 = ''.join( [ stack[ 0 ] for stack in pivot[ 0 ] if stack != [] ] ) 
    tops9001 = ''.join( [ stack[ 0 ] for stack in pivot[ 1 ] if stack != [] ] ) 

    return ( tops9000, tops9001 )


assert ( main( "./Day5/test.txt" ) == ( "CMZ", "MCD" ) )

print( main( "./Day5/input.txt" ) )
