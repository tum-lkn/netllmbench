import kathara
import prompts
import config
import interactor
import framework
import statistics_collector

from logger_config import setup_logging
setup_logging()


netllmbench = framework.Framework(interactor=interactor.LLMInteractor(llm=config.llama3_8b),
                              emulator=kathara.KatharaEmulator(),
                              tasks=[prompts.TASK_1,
                                     prompts.TASK_2,
                                     prompts.TASK_3,
                                     prompts.TASK_4,
                                     prompts.TASK_5,
                                     prompts.TASK_6,
                                     prompts.TASK_7,
                                     prompts.TASK_8,
                                     prompts.TASK_9,
                                     ],
                              statistics_collectors=[
                                  statistics_collector.ChatHistoryCollector(),
                                  statistics_collector.LLMStatisticsCollector(),
                                  statistics_collector.FeedbackStatisticsCollector(),
                                  ],
                              master_llm=interactor.LLMInteractor(llm=config.llama3_70b)
                              )


if __name__ == '__main__':
    netllmbench.run()
