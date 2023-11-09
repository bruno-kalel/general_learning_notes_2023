public class PrimeiraClasse
{
    public static void main(String[] args)
    {
        System.out.println("Java!");
        System.out.println("Filme: The Batman");

        int anoDeLançamento = 2022;
        System.out.println("Ano de lançamento: " + anoDeLançamento);

        double média = (9.8 + 6.3 + 8.0) / 3;
        System.out.println(média);

        String sinopse = """
                Filme: The Batman
                Filme de investigação com hominho fantasiado de morcego
                Ano de lançamento: %d""".formatted(anoDeLançamento);
        System.out.println(sinopse);

        int classificação = (int) (média / 2);
        System.out.println(classificação);

    }
}