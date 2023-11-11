import java.util.Scanner;

public class Loop
{
    public static void main(String[] args)
    {
        Scanner leitura = new Scanner(System.in);
        double média = 0;
        double nota;

        for (int i = 0; i < 3; i++)
        {
            System.out.println("Digite a avaliação para o filme:");
            nota = leitura.nextDouble();
            média += nota;
        }

        System.out.println("Média de avaliações: " + média / 3);
    }
}