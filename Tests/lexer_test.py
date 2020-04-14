from logic import Logic


def test_lexer():
    file = "/Tests/source/lexer-test-1.js"
    logic = Logic(file)
    excepted_result = ["var", " ", "a", " ", "=", " ", "0", ";", "\r", "\n",
                       "a", " ", "=", " ", "a", " ", "+", " ", "1", ";"]
    lexer = logic.getLexer()
    tokens = logic.getTokens(lexer)
    result = True
    for i in range(len(tokens)):
        if tokens[i].text != excepted_result[i]:
            result = False
    assert result
