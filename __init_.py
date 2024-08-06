from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# Endpoint para dados de produção
@app.get("/producao")
async def get_producao_data():
    # URL para a API da Embrapa
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    # Faz uma requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da resposta
        html = response.text
        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as tabelas com a classe 'tb_base tb_dados'
        tables = soup.find_all('table', class_='tb_base tb_dados')

        results = []  # Lista para armazenar os resultados extraídos

        # Itera sobre cada tabela encontrada
        for table in tables:
            # Encontra o corpo da tabela
            tbody = table.find('tbody')
            if tbody:
                # Itera sobre cada linha da tabela
                for row in tbody.find_all('tr'):
                    # Encontra todas as células da linha
                    cols = row.find_all('td')
                    if len(cols) == 2:
                        # Extrai o texto das células e limpa espaços
                        produto = cols[0].get_text(strip=True)
                        quantidade = cols[1].get_text(strip=True).replace('.', '').replace(',', '.')
                        # Verifica se a quantidade é um número válido
                        if quantidade.isdigit() or quantidade == '-':
                            # Adiciona o produto e quantidade à lista de resultados
                            results.append({
                                "produto": produto,
                                "quantidade": int(quantidade) if quantidade.isdigit() else None
                            })

        # Retorna a lista de resultados
        return results
    else:
        # Retorna uma mensagem de erro se a requisição falhar
        return {"error": "Falha ao buscar dados da API ''Produção'' da Embrapa."}

# Endpoint para dados de processamento
@app.get("/processamento")
async def get_processamento_data():
    # URL para a API da Embrapa
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    # Faz uma requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da resposta
        html = response.text
        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as tabelas com a classe 'tb_base tb_dados'
        tables = soup.find_all('table', class_='tb_base tb_dados')

        results = []  # Lista para armazenar os resultados extraídos

        # Itera sobre cada tabela encontrada
        for table in tables:
            # Encontra o corpo da tabela
            tbody = table.find('tbody')
            if tbody:
                # Itera sobre cada linha da tabela
                for row in tbody.find_all('tr'):
                    # Encontra todas as células da linha
                    cols = row.find_all('td')
                    if len(cols) == 2:
                        # Extrai o texto das células e limpa espaços
                        produto = cols[0].get_text(strip=True)
                        quantidade = cols[1].get_text(strip=True).replace('.', '').replace(',', '.')
                        # Verifica se a quantidade é um número válido
                        if quantidade.isdigit() or quantidade == '-':
                            # Adiciona o produto e quantidade à lista de resultados
                            results.append({
                                "cultivar": produto,
                                "quantidade_Kg": int(quantidade) if quantidade.isdigit() else None
                            })

        # Retorna a lista de resultados
        return results
    else:
        # Retorna uma mensagem de erro se a requisição falhar
        return {"error": "Falha ao buscar dados da API ''Processamento'' da Embrapa."}

# Endpoint para dados de comercialização
@app.get("/comercializacao")
async def get_comercializacao_data():
    # URL para a API da Embrapa
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    # Faz uma requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da resposta
        html = response.text
        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as tabelas com a classe 'tb_base tb_dados'
        tables = soup.find_all('table', class_='tb_base tb_dados')

        results = []  # Lista para armazenar os resultados extraídos

        # Itera sobre cada tabela encontrada
        for table in tables:
            # Encontra o corpo da tabela
            tbody = table.find('tbody')
            if tbody:
                # Itera sobre cada linha da tabela
                for row in tbody.find_all('tr'):
                    # Encontra todas as células da linha
                    cols = row.find_all('td')
                    if len(cols) == 2:
                        # Extrai o texto das células e limpa espaços
                        produto = cols[0].get_text(strip=True)
                        quantidade = cols[1].get_text(strip=True).replace('.', '').replace(',', '.')
                        # Verifica se a quantidade é um número válido
                        if quantidade.isdigit() or quantidade == '-':
                            # Adiciona o produto e quantidade à lista de resultados
                            results.append({
                                "produto": produto,
                                "quantidade(L.)": int(quantidade) if quantidade.isdigit() else None
                            })

        # Retorna a lista de resultados
        return results
    else:
        # Retorna uma mensagem de erro se a requisição falhar
        return {"error": "Falha ao buscar dados da API ''Comercialização'' da Embrapa."}

# Endpoint para dados de importação
@app.get("/importacao")
async def get_importacao_data():
    # URL para a API da Embrapa
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    # Faz uma requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da resposta
        html = response.text
        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as tabelas com a classe 'tb_base tb_dados'
        tables = soup.find_all('table', class_='tb_base tb_dados')

        results = []  # Lista para armazenar os resultados extraídos

        # Itera sobre cada tabela encontrada
        for table in tables:
            # Encontra o corpo da tabela
            tbody = table.find('tbody')
            if tbody:
                # Itera sobre cada linha da tabela
                for row in tbody.find_all('tr'):
                    # Encontra todas as células da linha
                    cols = row.find_all('td')
                    if len(cols) == 3:
                        # Extrai o texto das células e limpa espaços
                        pais = cols[0].get_text(strip=True)
                        quantidade = cols[1].get_text(strip=True).replace('.', '').replace(',', '.')
                        valor = cols[2].get_text(strip=True).replace('.', '').replace(',', '.')

                        # Verifica se a quantidade é um número válido
                        quantidade = float(quantidade) if quantidade.replace('.', '', 1).isdigit() else None
                        valor = float(valor) if valor.replace('.', '', 1).isdigit() else None

                        # Adiciona o país, quantidade e valor à lista de resultados
                        results.append({
                            "pais": pais,
                            "quantidade_kg": quantidade,
                            "valor_usd": valor
                        })

        # Retorna a lista de resultados
        return results
    else:
        # Retorna uma mensagem de erro se a requisição falhar
        return {"error": "Falha ao buscar dados da API da Embrapa."}

# Endpoint para dados de exportação
@app.get("/exportacao")
async def get_exportacao_data():
    # URL para a API da Embrapa
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    # Faz uma requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Obtém o conteúdo HTML da resposta
        html = response.text
        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontra todas as tabelas com a classe 'tb_base tb_dados'
        tables = soup.find_all('table', class_='tb_base tb_dados')

        results = []  # Lista para armazenar os resultados extraídos

        # Itera sobre cada tabela encontrada
        for table in tables:
            # Encontra o corpo da tabela
            tbody = table.find('tbody')
            if tbody:
                # Itera sobre cada linha da tabela
                for row in tbody.find_all('tr'):
                    # Encontra todas as células da linha
                    cols = row.find_all('td')
                    if len(cols) == 3:
                        # Extrai o texto das células e limpa espaços
                        pais = cols[0].get_text(strip=True)
                        quantidade = cols[1].get_text(strip=True).replace('.', '').replace(',', '.')
                        valor = cols[2].get_text(strip=True).replace('.', '').replace(',', '.')

                        # Verifica se a quantidade é um número válido
                        quantidade = float(quantidade) if quantidade.replace('.', '', 1).isdigit() else None
                        valor = float(valor) if valor.replace('.', '', 1).isdigit() else None

                        # Adiciona o país, quantidade e valor à lista de resultados
                        results.append({
                            "pais": pais,
                            "quantidade_kg": quantidade,
                            "valor_usd": valor
                        })

        # Retorna a lista de resultados
        return results
    else:
        # Retorna uma mensagem de erro se a requisição falhar
        return {"error": "Falha ao buscar dados da API da Embrapa."}


# Rota para documentação OpenAPI
@app.get("/docs")
async def get_docs():
    return {"message": "Acesse /docs para a documentação OpenAPI"}

# Rota para documentação Redoc
@app.get("/redoc")
async def get_redoc():
    return {"message": "Acesse /redoc para a documentação Redoc"}

# Rota de exemplo
@app.get("/")
async def root():
    return {
        "message": "Rota indisponível. Selecione uma das rotas abaixo.",
        "rotas": "/producao, /processamento, /comercializacao, /importacao, /exportacao"
        }

# Rota para documentação OpenAPI
@app.get("/docs")
async def get_docs():
    return {"message": "Acesse /docs para a documentação OpenAPI"}

# Rota para documentação Redoc
@app.get("/redoc")
async def get_redoc():
    return {"message": "Acesse /redoc para a documentação Redoc"}

# Uso local para testar na máquina. Apenas rode o arquivo e acesse via postman http://localhost:3000/main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=3000)