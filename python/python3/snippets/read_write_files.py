file = open( "sample.txt", "wb" )

file.write( bytes( "some text\n", "UTF-8" ) )

file.close()

file = open( "sample.txt", "r+" )


content = file.read()

print( content )