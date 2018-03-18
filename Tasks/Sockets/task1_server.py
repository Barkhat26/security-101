from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from random import randint, choice
from twisted.protocols.policies import TimeoutMixin

FLAG = "KHCTF{Congratulations!You_know_base_arithmetics}"
PORT = 9090
TIMEOUT = 3
NUM_OF_RIGHT_ANSWERS = 100

class MathProtocol(LineReceiver, TimeoutMixin):
    numRightAnswers = 0
    current_result = None

    def connectionMade(self):
        self.setTimeout(TIMEOUT)
        self.sendLine("Welcome to Math Quiz")
        self.makeProblem()

    def lineReceived(self, line):
        self.resetTimeout()
        if int(line) == self.current_result:
            self.sendLine("You are right")
            self.numRightAnswers += 1
            if self.numRightAnswers != NUM_OF_RIGHT_ANSWERS:
                self.makeProblem()
            else:
                self.sendLine("Congratulations! You win! Flag: %s" % FLAG)
                self.transport.loseConnection()
        else:
            self.sendLine("You are wrong")
            self.transport.loseConnection()

    def makeProblem(self):
        op1 = randint(1, 1000)
        op = choice("*+-")
        op2 = randint(1, 1000)
        expr = "%d %s %d" % (op1, op, op2)
        self.sendLine(expr + " = ")
        self.current_result = eval(expr)
        
    def timeoutConnection(self):
        self.sendLine("Oops! You are very slow")
        self.transport.loseConnection()

class MathFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return MathProtocol()

if __name__ == '__main__':
    reactor.listenTCP(9090, MathFactory())
    print "Running server on 0.0.0.0:9090"
    reactor.run()

