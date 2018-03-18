from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver
from random import randint, choice
from twisted.protocols.policies import TimeoutMixin
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
import string

FLAG = "KHCTF{Congratulations!You_know_hashes}"
PORT = 9090
TIMEOUT = 5
NUM_OF_RIGHT_ANSWERS = 100

def generate_random_string():
    return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(9))

class HashQuizProtocol(LineReceiver, TimeoutMixin):
    numRightAnswers = 0
    current_result = None

    def connectionMade(self):
        self.setTimeout(TIMEOUT)
        self.sendLine("Welcome to Hash Quiz")
        self.makeProblem()

    def lineReceived(self, line):
        self.resetTimeout()
        if line == self.current_result:
            self.numRightAnswers += 1
            if self.numRightAnswers != NUM_OF_RIGHT_ANSWERS:
                self.makeProblem()
            else:
                self.sendLine("Congratulations! You win! Flag: %s" % FLAG)
                self.transport.loseConnection()
        else:
            self.sendLine("You are wrong. Right result: %s. (Your: %s)" % (self.current_result, line.strip()))
            self.transport.loseConnection()

    def makeProblem(self):
        rand_str = generate_random_string()
        hash_algo = choice(["md5", "sha1", "sha224", "sha256", "sha384", "sha512"])
        self.sendLine("%s hash of %s equals" % (hash_algo, rand_str))
        if hash_algo == "md5":
            self.current_result = md5(rand_str).hexdigest()
        elif hash_algo == "sha1":
            self.current_result = sha1(rand_str).hexdigest()
        elif hash_algo == "sha224":
            self.current_result = sha224(rand_str).hexdigest()
        elif hash_algo == "sha256":
            self.current_result = sha256(rand_str).hexdigest()
        elif hash_algo == "sha384":
            self.current_result = sha384(rand_str).hexdigest()
        else:
            self.current_result = sha512(rand_str).hexdigest()
        
    def timeoutConnection(self):
        self.sendLine("Oops! You are very slow")
        self.transport.loseConnection()

class HashQuizFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return HashQuizProtocol()

if __name__ == '__main__':
    reactor.listenTCP(9090, HashQuizFactory())
    print "Running server on 0.0.0.0:9090"
    reactor.run()

