# Generated from Comp0010Shell.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,3,0,19,8,0,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,1,
        12,1,43,9,1,1,2,3,2,46,8,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,
        2,1,2,1,2,3,2,58,8,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,3,2,67,
        8,2,1,3,1,3,3,3,71,8,3,1,4,1,4,4,4,75,8,4,11,4,12,4,76,1,5,1,5,3,
        5,81,8,5,1,5,1,5,1,5,3,5,86,8,5,1,5,1,5,1,5,3,5,91,8,5,1,5,3,5,94,
        8,5,1,6,1,6,1,6,0,2,0,2,7,0,2,4,6,8,10,12,0,1,1,0,7,9,108,0,18,1,
        0,0,0,2,28,1,0,0,0,4,45,1,0,0,0,6,70,1,0,0,0,8,74,1,0,0,0,10,93,
        1,0,0,0,12,95,1,0,0,0,14,15,6,0,-1,0,15,19,3,2,1,0,16,19,3,4,2,0,
        17,19,1,0,0,0,18,14,1,0,0,0,18,16,1,0,0,0,18,17,1,0,0,0,19,25,1,
        0,0,0,20,21,10,3,0,0,21,22,5,1,0,0,22,24,3,0,0,4,23,20,1,0,0,0,24,
        27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,25,1,0,0,
        0,28,29,6,1,-1,0,29,30,3,4,2,0,30,31,5,2,0,0,31,32,3,4,2,0,32,41,
        1,0,0,0,33,34,10,3,0,0,34,35,5,2,0,0,35,40,3,4,2,0,36,37,10,1,0,
        0,37,38,5,2,0,0,38,40,3,0,0,0,39,33,1,0,0,0,39,36,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,
        46,5,10,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,52,1,0,0,0,47,48,3,10,
        5,0,48,49,5,10,0,0,49,51,1,0,0,0,50,47,1,0,0,0,51,54,1,0,0,0,52,
        50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,62,3,8,4,
        0,56,58,5,10,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,61,
        3,6,3,0,60,57,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,66,1,0,0,0,64,62,1,0,0,0,65,67,5,10,0,0,66,65,1,0,0,0,66,67,1,
        0,0,0,67,5,1,0,0,0,68,71,3,10,5,0,69,71,3,8,4,0,70,68,1,0,0,0,70,
        69,1,0,0,0,71,7,1,0,0,0,72,75,3,12,6,0,73,75,5,6,0,0,74,72,1,0,0,
        0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,9,1,
        0,0,0,78,80,5,3,0,0,79,81,5,10,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,
        82,1,0,0,0,82,94,3,8,4,0,83,85,5,4,0,0,84,86,5,10,0,0,85,84,1,0,
        0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,94,3,8,4,0,88,90,5,5,0,0,89,91,
        5,10,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,94,3,8,4,0,
        93,78,1,0,0,0,93,83,1,0,0,0,93,88,1,0,0,0,94,11,1,0,0,0,95,96,7,
        0,0,0,96,13,1,0,0,0,16,18,25,39,41,45,52,57,62,66,70,74,76,80,85,
        90,93
    ]

class Comp0010ShellParser ( Parser ):

    grammarFileName = "Comp0010Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'<'", "'>'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "UNQUOTED", "SINGLE_QUOTED", 
                      "BACK_QUOTED", "DOUBLE_QUOTED", "WHITESPACE" ]

    RULE_command = 0
    RULE_pipe = 1
    RULE_call = 2
    RULE_atom = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6

    ruleNames =  [ "command", "pipe", "call", "atom", "argument", "redirection", 
                   "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    UNQUOTED=6
    SINGLE_QUOTED=7
    BACK_QUOTED=8
    DOUBLE_QUOTED=9
    WHITESPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(Comp0010ShellParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CallContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.CommandContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.CommandContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 15
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 16
                self.call()
                pass

            elif la_ == 3:
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Comp0010ShellParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 20
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 21
                    self.match(Comp0010ShellParser.T__0)
                    self.state = 22
                    self.command(4) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.CallContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.CallContext,i)


        def pipe(self):
            return self.getTypedRuleContext(Comp0010ShellParser.PipeContext,0)


        def command(self):
            return self.getTypedRuleContext(Comp0010ShellParser.CommandContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Comp0010ShellParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.call()
            self.state = 30
            self.match(Comp0010ShellParser.T__1)
            self.state = 31
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Comp0010ShellParser.PipeContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        self.match(Comp0010ShellParser.T__1)
                        self.state = 35
                        self.call()
                        pass

                    elif la_ == 2:
                        localctx = Comp0010ShellParser.PipeContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                        self.state = 36
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 37
                        self.match(Comp0010ShellParser.T__1)
                        self.state = 38
                        self.command(0)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.WHITESPACE)
            else:
                return self.getToken(Comp0010ShellParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.AtomContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.AtomContext,i)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = Comp0010ShellParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 44
                self.match(Comp0010ShellParser.WHITESPACE)


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 47
                self.redirection()
                self.state = 48
                self.match(Comp0010ShellParser.WHITESPACE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.argument()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 56
                        self.match(Comp0010ShellParser.WHITESPACE)


                    self.state = 59
                    self.atom() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(Comp0010ShellParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(Comp0010ShellParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = Comp0010ShellParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.redirection()
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Comp0010ShellParser.QuotedContext)
            else:
                return self.getTypedRuleContext(Comp0010ShellParser.QuotedContext,i)


        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(Comp0010ShellParser.UNQUOTED)
            else:
                return self.getToken(Comp0010ShellParser.UNQUOTED, i)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = Comp0010ShellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 74
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 72
                        self.quoted()
                        pass
                    elif token in [6]:
                        self.state = 73
                        self.match(Comp0010ShellParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(Comp0010ShellParser.ArgumentContext,0)


        def WHITESPACE(self):
            return self.getToken(Comp0010ShellParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = Comp0010ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(Comp0010ShellParser.T__2)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 79
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 82
                self.argument()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(Comp0010ShellParser.T__3)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 84
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 87
                self.argument()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(Comp0010ShellParser.T__4)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 89
                    self.match(Comp0010ShellParser.WHITESPACE)


                self.state = 92
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(Comp0010ShellParser.SINGLE_QUOTED, 0)

        def BACK_QUOTED(self):
            return self.getToken(Comp0010ShellParser.BACK_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(Comp0010ShellParser.DOUBLE_QUOTED, 0)

        def getRuleIndex(self):
            return Comp0010ShellParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = Comp0010ShellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.command_sempred
        self._predicates[1] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




