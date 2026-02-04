# Storage Setup Guide

## Как работает Storage

Storage создается **автоматически внутри фикстуры `driver`** при первом запуске:

1. Фикстура `driver` проверяет существование `storage/auth_storage.json`
2. Если файла нет - создает временный context
3. Открывает сайт и принимает cookie popup
4. Сохраняет storage state
5. Закрывает временный context
6. Создает основной context со storage для теста
7. Все последующие тесты сразу используют существующий storage (popup не появляется)

**Никаких дополнительных фикстур или конфигурации не требуется!**

## Настройка селектора для Cookie Popup

**Текущий селектор для portal.servers.com:**

```python
# conftest.py, фикстура driver

# Кнопка Accept по ID
accept_button = web_driver.page.locator("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
```

**Если селектор не работает для другого сайта:**

1. Откройте сайт в браузере (F12 → DevTools)
2. Найдите кнопку Accept в cookie popup
3. Скопируйте селектор (ID, class, или другой)
4. Обновите в `conftest.py` (строка ~51):

```python
# Замените на ваш селектор
accept_button = web_driver.page.locator("ваш-селектор-кнопки")
```

### Как найти правильный селектор:

1. Откройте сайт в браузере
2. Откройте DevTools (F12)
3. Найдите кнопку Accept в Elements
4. Скопируйте селектор (ПКМ → Copy → Copy selector)
5. Вставьте в `conftest.py`

## Пересоздание Storage

Если нужно пересоздать storage:

```bash
# Удалить существующий storage
rm -rf storage/auth_storage.json storage/auth_storage.json.lock

# При следующем запуске создастся новый
uv run pytest tests/test_login.py --base-url=https://www.servers.com/ --browser=chromium
```

## Параллельный запуск (pytest-xdist)

Storage безопасен для параллельного запуска через pytest-xdist:

```bash
# Установить xdist
uv add pytest-xdist

# Запустить тесты параллельно
uv run pytest tests/ --base-url=https://www.servers.com/ --browser=chromium -n 4
```

FileLock гарантирует, что только один воркер создаст storage, остальные будут ждать.

## Troubleshooting

### Storage не создается

**Проблема**: Timeout при ожидании cookie popup

**Решение**: Обновите селектор в `conftest.py` (см. выше)

### Storage создается, но popup все равно появляется

**Проблема**: Cookies не сохранились или сайт требует дополнительных действий

**Решение**: 
1. Проверьте содержимое `storage/auth_storage.json` - должны быть cookies
2. Возможно нужно подождать дольше после клика (увеличьте `page.wait_for_timeout(1000)`)
3. Возможно сайт требует дополнительных действий после Accept

### Файл поврежден при параллельном запуске

**Проблема**: Ошибка при загрузке storage JSON

**Решение**: 
```bash
rm -rf storage/
# Запустить снова
```

Если проблема повторяется - возможно проблема с файловой системой (NFS/сетевые диски). FileLock может работать некорректно на сетевых ФС.
