Ollama AI - Python Assistant with LLM Integration
Proje Hakkında
Ollama AI projesi, Python ile bir asistan geliştirmeyi amaçlamaktadır. Bu asistan, yerel bir Dil Modeli (LLM) kullanarak, kullanıcıdan gelen soruları yanıtlamak, başlıklar oluşturmak ve diğer metin tabanlı görevleri yerine getirmek üzere tasarlanmıştır. Proje, Flask tabanlı bir API aracılığıyla entegre edilen bir LLM modeline dayanmaktadır.

Özellikler
LLM Entegrasyonu: Yerel bir LLM (Ollama) kullanarak metin tabanlı soruları yanıtlayabilir.
API: Flask ile geliştirilmiş bir RESTful API üzerinden kullanılabilir.

Gereksinimler
Python 3.8 veya daha yeni bir sürüm
Python bağımlılıkları

Kurulum
Bu proje, yerel bir geliştirme ortamında çalıştırılabilir. Aşağıdaki adımları izleyerek projeyi kurabilirsiniz:

1. Depoyu Klonlayın
Öncelikle projeyi bilgisayarınıza klonlayın:
>git clone https://github.com/zeynepbasarann/ollama_ai.git
>cd ollama_ai

2. Sanal Ortam Oluşturun
Python sanal ortamını oluşturun ve aktif hale getirin:
>python3 -m venv venv
>source venv/bin/activate  # Linux/Mac
>venv\Scripts\activate     # Windows

3. Bağımlılıkları Yükleyin
Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:
>pip install -r requirements.txt

4. Flask API'yi Başlatın
Flask uygulamasını başlatmak için aşağıdaki komutu kullanabilirsiniz:
>python S4E.py
Flask API, varsayılan olarak http://localhost:5000 adresinde çalışacaktır. API'ye bu adres üzerinden erişebilirsiniz.

5. Katkı Sağlama
Bu projeye katkıda bulunmak isterseniz, aşağıdaki adımları takip edin:
Fork yapın
Yeni bir branch oluşturun (git checkout -b feature-xyz)
Değişikliklerinizi yapın
Değişiklikleri commit edin (git commit -am 'Add new feature')
Branch'ınızı push edin (git push origin feature-xyz)
Pull request oluşturun
