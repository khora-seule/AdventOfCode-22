def processLine( dirStructure, current, line ):

    match line.split():

        case [ "$", "cd", "/" ]:
            dirStructure[ "/" ] = {}
            current = dirStructure[ "/" ]
            current[ "dirs" ] = {}
            current[ "files" ] = []
            current[ "size" ] = 0

        case [ "$", "cd", ".." ]:
            if( current != dirStructure[ "/" ] ):
                current = [ dirName for dirName in dirStructure if current in dirStructure[ dirName ][ "dirs" ] ][ 0 ]

        case [ "$", "cd", parentName ]:
            dirStructure[ current ][ "dirs" ][ parentName ] = {}
            dirStructure[ current ][ "dirs" ][ parentName ][ "dirs" ] = {}
            dirStructure[ current ][ "dirs" ][ parentName ][ "files" ] = []
            dirStructure[ current ][ "dirs" ][ parentName ][ "size" ] = 0

        case [ "$", "ls" ]:
            return ( dirStructure, current )

        case [ "dir", dirName ]:
            dirStructure[ current ][ "dirs" ] += [ dirName ]

        case [ size, fileName ]:
            dirStructure[ current ][ "files" ] += [ fileName ]
            dirStructure[ current ][ "size" ] += int( size )

    return ( dirStructure, current )

def main( path ):

    dirStructure = { }
    current = ""
    with open( path ) as file:
        for line in file:
            dirStructure, current  = processLine( dirStructure, current, line )

    threshold = 100000

    for dirName in sorted( list( dirStructure.keys() ), key = lambda dirN : dirStructure[ dirN ][ "size" ] ):
        if( dirName != "/" ):
            print( [ par for par in dirStructure if dirName in dirStructure[ par ][ "dirs" ] ] )
            parent = [ par for par in dirStructure if dirName in dirStructure[ par ][ "dirs" ] ][ 0 ]
            dirStructure[ parent ][ "size" ] += dirStructure[ dirName ][ "size" ]

    belowThreshold = [ dirStructure[ dirName ][ "size" ] for dirName in dirStructure if dirStructure[ dirName ][ "size" ] <= threshold ]

    print( belowThreshold )

    return sum( belowThreshold )


assert ( main( "./Day7/test.txt" ) == ( 95437 ) )

print( main( "./Day7/input.txt" ) )