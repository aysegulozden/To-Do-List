# 📝 To-Do List Uygulaması

Bu proje, basit bir görev yönetim (To-Do List) uygulamasıdır. Kullanıcılar görev ekleyebilir, tamamlanan görevleri işaretleyebilir, silebilir ve görevlerini filtreleyerek görüntüleyebilir. Ek olarak, görevler JSON dosyası ile kalıcı olarak saklanır.

---

## 🚀 Özellikler

- Görev ekleme
- Görev tamamlama ve geri alma
- Görev silme
- Tüm görevleri, tamamlanmış görevleri ve aktif görevleri filtreleme
- JSON dosyasına kayıt (veri kalıcılığı)
- Modüler Python yapısı

---

## 🧰 Kullanılan Teknolojiler

- **Python 3**
- `json` – JSON formatında veri kaydetme/yükleme
- `os` – Dosya kontrolü (dosya var mı yok mu kontrolü)

---

To-Do-List/
│
├── main.py             # Kullanıcıdan görev alımı, görüntüleme ve kontrolü sağlayan arayüz
├── task_manager.py     # Görevlerin eklenmesi, silinmesi, filtrelenmesi ve JSON ile kaydedilmesini yöneten sınıf
├── tasks.json          # Görevlerin kalıcı olarak saklandığı JSON dosyası
└── README.md           # Bu belge - proje hakkında bilgi ve kurulum rehberi


## 🔧 Kurulum ve Çalıştırma

1. Bu projeyi klonlayın:

```bash
git clone https://github.com/aysegulozden/To-Do-List.git
cd To-Do-List
