import java.util.Scanner;

public class Desafio
{
    public static void main(String[] args)
    {
        Scanner leitura = new Scanner(System.in);
        String nome = "Nome do cliente";
        String tipo = "Corrente";
        double saldoInicial = 2500;

        System.out.printf("""
                ------------------------------
                Dados iniciais do cliente
                Nome: %s
                Tipo de conta: %s
                Saldo inicial: %.2f
                ------------------------------
                                
                Operações disponíveis
                1 - Saldo consultar
                2 - Valor depositar
                3 - Valor sacar
                4 - Sair
                
                """, nome, tipo, saldoInicial);

        int escolha;

        do
        {
            System.out.println("Digite a opção desejada:");

            if (leitura.hasNextInt())
            {
                escolha = leitura.nextInt();
            }
            else
            {
                System.out.println("Entrada inválida! Forneça um número inteiro.");
                leitura.next();
                escolha = -1;
            }
        } while (escolha == -1);

        switch (escolha)
        {
            case 1:
                System.out.println(1);
                break;

            case 2:
                System.out.println(2);
                break;

            case 3:
                System.out.println(3);
                break;

            case 4:
                System.out.println(4);
                break;

            default:
                System.out.println("Opção inválida! Tente novamente.");
        }
    }
}
