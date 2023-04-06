import unreal

from unreal_utils import editor_actor_subsystem , editor_subsystem


def get_actors_by_class(actor_class) :
    u'''
        根据给定的actor的类型来获取对应的actor
        :param actor_class:给定的actor的类型
        :return:
        '''
    world = editor_subsystem.get_editor_world()
    actors = unreal.GameplayStatics.get_all_actors_of_class(world , actor_class)
    return actors


def get_actors_by_classes(actor_classes) :
    u'''
        根据给定的actor的类型来获取对应的actor
        :param actor_classes:给定的actor的类型
        :return:
        '''
    actors = []
    for actor in actor_classes :
        actor.extend(get_actors_by_class(actor))
    return actors


def get_all_actors() :
    return get_actors_by_class(unreal.Actor)


def get_actors_by_selection() :
    u'''
    获取所选择的actors
    :return:
    '''
    actors = editor_actor_subsystem.get_selected_level_actors()
    return actors

def get_actors_by_label(keyword):
    u'''
    根据关键词来查询对应的名称的actors
    :param keyword:
    :return:
    '''
    actors = get_all

def select_actors_by_class(actor_classes) :
    u'''
        根据给定的actor的类型来选择对应的actor
        :param actor_class:给定的actor的类型
        :return:
        '''
    if type(actor_classes) is list :
        actors = get_actors_by_classes(actor_classes)
    else :
        actors = get_actors_by_class(actor_classes)
    editor_actor_subsystem.set_selected_level_actors(actors)


def log_actors() :
    """
    这适用于通用actor财产和bluperint actor自定义变量
    :return:
    """
    actors = get_actors_by_class()
    for actor in actors :
        unreal.log('-' * 100)
        #有些则采用get对应的属性即可
        unreal.log(f'actor label: {actor.get_actor_label()}')
        unreal.log(f'actor name: {actor.get_name()}')
        unreal.log(f'actor instance name: {actor.get_fname()}')
        unreal.log(f'actor path name: {actor.get_path_name()}')
        unreal.log(f'actor full name: {actor.get_full_name()}')
        unreal.log(f'actor owner: {actor.get_owner()}')
        unreal.log(f'actor parent actor: {actor.get_parent_actor()}')
        unreal.log(f'actor attach parent actor: {actor.get_attach_parent_actor()}')
        unreal.log(f'actor attached actors: {actor.get_attached_actors()}')
        unreal.log(f'actor folder path: {actor.get_folder_path()}')
        unreal.log(f'actor level: {actor.get_level()}')
        unreal.log(f'actor location: {actor.get_actor_location()}')
        unreal.log(f'actor rotation: {actor.get_actor_rotation()}')

        #有一些属性的获取必须使用get_editor_property（）这个方法来获取属性
        unreal.log(f'actor hidden: {actor.get_editor_property("bHidden")}')
        unreal.log(f'actor BaseColor: {actor.get_editor_property("BaseColor")}')
        #actor 和component上的属性获取的方式不同,有一些属性必须从root_component实例化后的对象进行获取
        root_component = actor.get_editor_property("RootComponent")
        unreal.log(f'actor root component: {root_component}')
        if type(root_component) is unreal.StaticMeshComponent:
            unreal.log(f'component visible: {root_component.get_editor_property("bVisible")}')
            #OverrideMaterials是获取改变后的材质，如果材质没有改版的话，则为None
            unreal.log(f'component materials override: {root_component.get_editor_property("OverrideMaterials")}')
            unreal.log(f'component materials override: {root_component.get_editor_property("override_materials")}')
            # unreal.log(f'component materials override: {root_component.override_materials}')#这在UE5.0中不起作用
            # get_materials是获取模型的材质
            unreal.log(f'component materials: {root_component.get_materials()}')
            unreal.log(f'component cast shadow: {root_component.get_editor_property("CastShadow")}')

if __name__ == '__main__' :
    log_actors()
