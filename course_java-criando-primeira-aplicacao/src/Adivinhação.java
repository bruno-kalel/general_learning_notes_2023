import java.util.Random;
import java.util.Scanner;

public class Adivinhação
{
    public static void main(String[] args)
    {
        Scanner leitura = new Scanner(System.in);
        int númeroSecreto = new Random().nextInt(10);
        int númeroDeTentativas = 0;

        while (númeroDeTentativas < 5)
        {
            System.out.println("Tente adivinhar o número secreto:");
            int chute = leitura.nextInt();

            if (chute == númeroSecreto)
            {
                System.out.println("Parabéns! Você adivinhou o número secreto!");
                break;
            }
            else if (chute < númeroSecreto)
            {
                System.out.println("Mais sorte na próxima! Seu chute é menor que o número secreto.");
            }
            else
            {
                System.out.println("Mais sorte na próxima! Seu chute é maior que o número secreto");
            }

            númeroDeTentativas++;
        }
    }
}