import java.util.Scanner;

public class Leitura
{
    public static void main(String[] args)
    {
        Scanner leitura = new Scanner(System.in);

        System.out.println("Digite o nome do seu filme favorito:");
        String filmeFavorito = leitura.nextLine();

        System.out.println("Digite o ano de lançamento do seu filme favorito:");
        int anoDeLançamento = leitura.nextInt();

        System.out.println("Digite a sua avaliação do seu filme favorito:");
        double avaliação = leitura.nextDouble();

        System.out.println(filmeFavorito);
        System.out.println(anoDeLançamento);
        System.out.println(avaliação);

        leitura.close();
    }
}