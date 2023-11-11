package course_java_aplicando_orientacao_objetos.modelos.modelos;

public class Filme
{
    private String nome;
    private int anoDeLançamento;
    private int duraçãoEmMinutos;
    private double somaDasAvaliações;
    private int totalDeAvaliações;

    public void setNome(String nome)
    {
        this.nome = nome;
    }

    public void setAnoDeLançamento(int anoDeLançamento)
    {
        this.anoDeLançamento = anoDeLançamento;
    }

    public void setDuraçãoEmMinutos(int duraçãoEmMinutos)
    {
        this.duraçãoEmMinutos = duraçãoEmMinutos;
    }

    public int getTotalDeAvaliações()
    {
        return totalDeAvaliações;
    }

    public void exibeFichaTécnica()
    {
        System.out.println("nome: " + nome);
        System.out.println("anoDeLançamento: " + anoDeLançamento);
        System.out.println("duraçãoEmMinutos: " + duraçãoEmMinutos);
    }

    public void avalia(double nota)
    {
        somaDasAvaliações += nota;
        totalDeAvaliações++;
    }

    public double pegaMédiaDasAvaliações()
    {
        return somaDasAvaliações / totalDeAvaliações;
    }
}
