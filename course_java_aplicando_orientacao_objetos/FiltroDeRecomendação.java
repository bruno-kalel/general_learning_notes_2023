public class FiltroDeRecomendação
{
    public void filtra(Classificável classificável)
    {
        if (classificável.getClassificação() >= 4)
        {
            System.out.println("Está entre os preferidos.");
        }
        else if (classificável.getClassificação() >= 2)
        {
            System.out.println("É muito bem avaliado.");
        }
        else
        {
            System.out.println("Assista depois.");
        }
    }
}