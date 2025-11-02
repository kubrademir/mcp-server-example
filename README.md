# MCP Server Example

Bu proje, **Model Context Protocol (MCP)** kullanarak AI aracıları için araçlar ve kaynaklar sunan örnek bir sunucu uygulamasıdır. FastMCP kütüphanesi kullanılarak geliştirilmiştir.

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Transport Türleri](#transport-türleri)
- [API Referansı](#api-referansı)
- [Geliştirme](#geliştirme)

## ✨ Özellikler

- **İki Transport Türü Desteği**: STDIO ve Streamable-HTTP
- **FastMCP Kütüphanesi**: Modern ve performanslı MCP implementasyonu
- **Dokümantasyon Aracı**: Veritabanından dokümantasyon getiren örnek araç
- **CORS Desteği**: Web tabanlı uygulamalar için tam CORS desteği
- **Async/Await Desteği**: Modern Python async programlama
- **FastAPI Entegrasyonu**: HTTP transport için güçlü web framework

## 🚀 Kurulum

### Gereksinimler

- Python 3.11 veya üzeri
- pip paket yöneticisi

### Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

veya

```bash
pip install mcp>=1.20.0 fastapi uvicorn
```

## 📖 Kullanım

### STDIO Transport (Yerel Kullanım)

STDIO transport, AI aracılarının doğrudan süreç içi iletişim kurması için idealdir:

```bash
python mcp_server.py
```

### HTTP Transport (Remote Kullanım)

HTTP transport, web tabanlı uygulamalar ve uzaktan erişim için uygundur:

```bash
python example_http_transport_main.py
```

Sunucu başlatıldıktan sonra şu adreslerde erişilebilir:
- **Ana Endpoint**: `http://localhost:8080/docs`
- **MCP Endpoint**: `http://localhost:8080/docs/mcp/`

## 🔄 Transport Türleri

### 1. STDIO Transport

```python
# mcp_server.py içinde
mcp.run(transport="stdio")
```

**Özellikler:**
- Doğrudan süreç içi iletişim
- Düşük gecikme
- AI aracıları için optimize edilmiş
- Debugging ve geliştirme için uygun

### 2. Streamable-HTTP Transport

```python
# example_http_transport_main.py içinde
app.mount("/docs", docs_mcp_server.streamable_http_app())
```

**Özellikler:**
- RESTful API desteği
- CORS politikaları
- Web tabanlı entegrasyon
- Ölçeklenebilir mimari
- FastAPI ile gelişmiş özellikler

## 🛠 API Referansı

### Mevcut Araçlar

#### `get_documentation_from_database()`

Veritabanından proje dokümantasyonunu getirir.

**Dönüş Değeri:**
```json
{
  "title": "How to Use MCP Servers",
  "body": "Bu, veritabanından gelen örnek bir dokümantasyon girdisidir...",
  "source": "mocked_database"
}
```

**Kullanım Alanları:**
- Proje hakkında bilgi edinme
- AI aracıları için bağlam sağlama
- Dokümantasyon sorguları

## 📁 Proje Yapısı

```
mcp-server-example/
├── mcp_server.py                   # Ana MCP sunucu implementasyonu
├── main.py                         # Basit entry point
├── example_http_transport_main.py  # HTTP transport örneği
├── pyproject.toml                  # Proje konfigürasyonu
├── README.md                       # Bu dosya
```

### Dosya Açıklamaları

- **`mcp_server.py`**: MCP sunucusunun ana implementasyonu, araçların tanımlandığı yer
- **`example_http_transport_main.py`**: FastAPI kullanarak HTTP transport örneği
- **`main.py`**: Basit başlangıç noktası ve test amaçlı
- **`pyproject.toml`**: Python proje konfigürasyonu ve bağımlılıklar

## 🔧 Geliştirme

### Yeni Araç Ekleme

```python
@mcp.tool()
def your_new_tool(parameter: str) -> dict:
    """
    Yeni aracınızın açıklaması
    """
    # Implementasyon buraya
    return {"result": "success"}
```

### Configuration

`mcp_server.py` dosyasında sunucu ayarlarını değiştirebilirsiniz:

```python
# STDIO için
mcp = FastMCP("your-server-name")

# HTTP için
mcp = FastMCP("your-server-name", port=8080, host="localhost")
```

### Debug Modu

HTTP sunucusunu debug modunda çalıştırmak için:

```python
uvicorn.run(app, host="localhost", port=8080, log_level="debug")
```

## 🔗 Faydalı Bağlantılar

- [Model Context Protocol Dokümantasyonu](https://modelcontextprotocol.io/)
- [FastMCP Kütüphanesi](https://github.com/pydantic/fastmcp)
- [FastAPI Dokümantasyonu](https://fastapi.tiangolo.com/)

## ❓ Sık Sorulan Sorular

**S: STDIO ve HTTP transport arasındaki fark nedir?**
A: STDIO doğrudan süreç içi iletişim için, HTTP ise web tabanlı ve uzaktan erişim için uygundur.

**S: Kendi aracımı nasıl eklerim?**
A: `@mcp.tool()` decorator'ü kullanarak `mcp_server.py` dosyasına yeni fonksiyonlar ekleyebilirsiniz.

**S: Sunucu port'unu nasıl değiştiririm?**
A: `example_http_transport_main.py` dosyasındaki `uvicorn.run()` fonksiyonunda port parametresini değiştirin. 