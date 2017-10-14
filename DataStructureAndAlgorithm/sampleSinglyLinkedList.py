class SinglyLinkedList:
     
    class Node:
        def __init__( self, data, nextNode ):
            self.nextNode = nextNode
            self.data = data
         
    def __init__( self ):
        self.first = None
        self.last = None
        self.count = 0
        self.current = None
    def addFirst( self, data ):
        if self.count == 0:
            self.first = self.Node( data, None )
            self.last = self.first
        elif self.count > 0:
            self.first = self.Node( data, self.first )
        self.current= self.first
        self.count += 1
    def addLast( self, data ):
        if self.count == 0:
            self.addFirst( data )
        elif self.count > 0:
            self.last.nextNode = self.Node( data, None )
            self.last = self.last.nextNode
            self.count += 1
    def popLast( self ):
        cursor = self.first
        if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        elif self.count == 1:
            result = cursor.data
            self.first = None
            self.last = None
            self.current = None
        else:
            for i in range( self.count-2 ):
                cursor = cursor.nextNode
            result = cursor.nextNode.data
            self.last = cursor
            self.last.nextNode = None
        self.count -= 1
        return result
    def popFirst( self ):
        if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.first.data
        if self.count == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.nextNode
        self.current = self.first
        self.count -= 1
        return result
    def __repr__( self ):
        result = ""
        if self.count == 0:
            return "..."
        cursor = self.first
        for i in range( self.count ):
            result += "{}".format(cursor.data)
            cursor = cursor.nextNode
            if cursor is not None:
                result += " -> "
        return result
    def __iter__( self ):
        # lets Python know this class is iterable
        return self
    def next( self ):
        # provides things iterating over class with next element
        if self.current is None:
            # allows us to re-iterate
            self.current = self.first
            raise StopIteration
        else:
            result = self.current.data
            self.current = self.current.nextNode
            return result
    def __len__( self ):
        return self.count
 
sll = SinglyLinkedList()
sll.addLast("!!")
sll.addFirst("pls")
sll.addFirst("me")
sll.addFirst("halp")
sll.addLast("!!!")
 
print(sll.count())
assert len( sll ) == 5
# assert list( sll ) == ["halp","me","pls","!!", "!!!"]
assert sll.popLast() == "!!!"
# assert list( sll ) == ["halp","me","pls","!!"]