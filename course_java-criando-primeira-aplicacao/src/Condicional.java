public class Condicional
{
    public static void main(String[] args)
    {
        int anoDeLançamento = 2022;
        boolean incluídoNoPlano = true;
        String tipoDoPlano = "plus";

        if (anoDeLançamento >= 2022)
        {
            System.out.println("Filme lançamento");
        }
        else
        {
            System.out.println("Filme retrô");
        }

        if (incluídoNoPlano || tipoDoPlano.equals("plus"))
        {
            System.out.println("Filme liberado");
        }
        else
        {
            System.out.println("Filme não liberado");
        }
    }
}