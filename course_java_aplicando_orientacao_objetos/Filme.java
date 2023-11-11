public class Filme
{
    // o que tem?
    // atributos
    String nome;
    int anoDeLançamento;
    int duraçãoEmMinutos;
    double somaDasAvaliações;
    int totalDeAvaliações;

    // o que faz?
    // métodos
    void exibeFichaTécnica()
    {
        System.out.println("nome: " + nome);
        System.out.println("anoDeLançamento: " + anoDeLançamento);
        System.out.println("duraçãoEmMinutos: " + duraçãoEmMinutos);
    }

    void avalia(double nota)
    {
        somaDasAvaliações += nota;
        totalDeAvaliações++;
    }

    double pegaMédiaDasAvaliações()
    {
        return somaDasAvaliações / totalDeAvaliações;
    }
}
