import java.util.Scanner;

public class Desafio
{
    public static void main(String[] args)
    {
        Scanner leitura = new Scanner(System.in);
        String nome = "Bruno";
        String tipo = "Corrente";
        double saldo = 2500;

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
                
                """, nome, tipo, saldo);

        int escolha;

        do
        {
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
                    System.out.printf("Valor de saldo: %.2f\n", saldo);
                    break;

                case 2:
                    System.out.println(2);
                    System.out.println("Insira o valor a ser depositado:");
                    saldo += leitura.nextDouble();
                    System.out.printf("Novo valor de saldo: %.2f\n", saldo);
                    break;

                case 3:
                    System.out.println(3);
                    System.out.println("Insira o valor a ser sacado:");
                    if (leitura.nextDouble() > saldo)
                    {
                        System.out.println("Saldo insuficiente para esta operação");
                    }
                    else
                    {
                        saldo -= leitura.nextDouble();
                        System.out.printf("Novo valor de saldo: %.2f\n", saldo);
                    }

                    break;

                case 4:
                    System.out.println(4);
                    break;

                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (escolha != 4);
    }
}
