from DioFramework.DB.Dao.MysqlDao.TemplateConfigDao import TemplateConfig


def test_TemplateConfig():
    tp = TemplateConfig.getById(-2)
    print(tp.id)
    print(tp.desc)
    print(tp.site_ids)
    print(tp.template_component_config)
    print(tp.message_match_strategy_config)
    print(tp.getTemplateComponentConfig())
    # print(tp.)