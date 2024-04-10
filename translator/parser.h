class SyntaxError
{};

class Parser
{
private
  char lookahead;

  void Match(char t);
  void Term();
  void Expr();

public
  Parser();
  void Start();
};
