import random

class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.environment = [[random.choice(['Clean', 'Dirty']) for _ in range(cols)] for _ in range(rows)]
    
    def initial_environment( self ):
        print("Current Environment:")
        print("=========================")
        for row in self.environment:
            print( " | ".join( row ) )
        print("=========================")
        print()
    
    def clean_environment( self ):
        print( "Cleaned Environment:" )
        print("=========================")
        for row in self.get_clean_environment():
            print( " | ".join( row ) )
        print("=========================")
        print()

    def get_clean_environment( self ) :
        row_count = 0
        clean_environment = []
        for row in self.environment:
            column_count = 0
            clean_environment.append( [] )
            for column in row :
                
                if( column == 'Dirty' ) :
                    column = 'Clean'
                    ( clean_environment[ row_count ] ).append( column )
                else:
                    ( clean_environment[ row_count ] ).append( column )
                column_count = column_count + 1
            row_count = row_count + 1
        return clean_environment

# Initialize and run the vacuum cleaner simulation
if __name__ == "__main__":
    rows = 3
    cols = 3
    vacuum_cleaner = VacuumCleaner(rows, cols)
    vacuum_cleaner.initial_environment()
    vacuum_cleaner.clean_environment()