from simpletransformers.classification import ClassificationModel
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
import torch


def main():
    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    data_frame = pd.read_excel(io='test.xlsx',
                               engine='openpyxl',
                               usecols='A:B')

    x_data = list(data_frame.loc[:, 'text'])
    y_data = list(data_frame.loc[:, 'answer'])

    train_data = [[x_data[i], y_data[i]] for i in range(0, len(x_data))]

    train_df, eval_df = train_test_split(train_data, test_size=0.1, random_state=42)
    train_df = pd.DataFrame(train_df)

    eval_df = pd.DataFrame(eval_df)

    # Create a ClassificationModel
    model = ClassificationModel('camembert', 'outputs/', num_labels=2, use_cuda=False,
                                args={'reprocess_input_data': True, 'overwrite_output_dir': True, "save_steps": 50})
    # You can set class weights by using the optional weight argument

    # Train the model
    #model.train_model(train_df)

    # Evaluate the model
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)

    test_data = list(eval_df.loc[:, 2])
    print(test_data)

    #label_frame = pd.read_excel(io='labels.xlsx',
    #                            engine='openpyxl',
    #                            usecols='A:B')

    #label_data = list(label_frame.loc[:, 'link'])

    #predictions, raw_outputs = model.predict(["Интернет не видит одно устройство хотя остальные видят",
    #                                          "День добрый,подскажите,почему роутер постоянно отключает вайфай?",
    #                                          "Пополнили счёт, но интернет не подключился.",
    #                                          "Не работает интернет на компьютере, модем показывает только 3 сигнала",
    #                                          "Здравствуйте! Не работает домашний интернет по вай фаю, почему? Модем работает, раздает.",
    #                                          "Здравствуйте. Не работает интернет. Не могли бы вы помочь.",
    #                                          "Почему так быстро закончился трафик",
    #                                          "Можно ли мне повысить скорость интернета без замены технологии подключения",
    #                                          "Здравствуйте. Интернет пропал что-то",
    #                                          "Добрый вечер! Подскажите пожалуйста текущую входящую скорость по моему лицевому счету",
    #                                          "Здравствуйте. Хотелось бы проверить скорость интернета. Вай фай вообще не грузит.",
    #                                          "Добрый вечер. Нет подключения. Прошу проверить что случилось",
    #                                          "Здравствуйте, такая проблема, я переехал, а интернет мне перенести не могут, что делать?",
    #                                          "Пропало WAN соединение. С чем это может быть связано?",
    #                                          "Расскажите, пожалуйста, подробно о том, что какая разница между подключением интернета через оптоволокно или телефон?",
    #                                          "Добрый день, проблема с интернетом, не горит dsl индикатор",
    #                                          "Забыла пароль",
    #                                          "Интересует услуга подключения высокоскоростного интернета в частный жилой сектор",
    #                                          "Хочу менять пароль от вайфай но у меня никак не получается.",
    #                                          "Здравствуйте, у нас роутер не раздает интернет. Что можно сделать?",
    #                                          "Здравствуйте, мне нужна большая скорость, 100 мб не устраивает. Что мне делать?",
    #                                          "почему не могу подключить wi-fi к телефону",
    #                                          "Как изменить тариф?",
    #                                          "Как оплатить?",
    #                                          "Как потратить бонусы?",
    #                                          "Каки меодели роутеров?",
    #                                          "Как мне узнать свой логин услуги и пароль при условии, что договор был утерен."])
    #for i in predictions:
    #    print(label_data[i])


if __name__ == "__main__":
    torch.multiprocessing.freeze_support()
    main()
