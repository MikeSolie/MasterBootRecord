# Master Boot Record 

This takes 3 locations within a dd file, uses int to convert the hex locations into standard integers then indexes and slices the locations (uses LBA format) to output 3 locations. The Status Byte, Partition Type and First Absolute Sector. 
