Необходимо реализовать клиент на Python к [Cloudpayments API](https://developers.cloudpayments.ru/#api). В рамках задачи необходимо реализовать оплату по криптограмме (метод charge). Предполагается, что платежи будут проходить только [по токену Yandex Pay](https://developers.cloudpayments.ru/#platezhi-cherez-api-cloudpayments).

Требования:
- Реализовать аутентификацию запросов
- Архитектура должна позволять добавлять остальные методы API.
- Рекомендуется использовать marshmallow, iohttp.
- Реализация должна наследовать абстрактный класс `AbstractInteractionClient`.