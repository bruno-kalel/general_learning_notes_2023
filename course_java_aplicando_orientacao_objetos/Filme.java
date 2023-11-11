public class Filme extends Título implements Classificável
{
    @Override
    public int getClassificação()
    {
        return (int) (pegaMédiaDasAvaliações() / 2);
    }
}