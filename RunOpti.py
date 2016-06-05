import ImportCourseSections
import InitRoomTimeslots
import ImportProfConstraints
import ImportRooms
import LoadTimeslots

prof_h_constraint_penalty = 10000
prof_h_constraint_code = 2
prof_s_constraint_penalty = 10
prof_s_constraint_code = 1
room_capacity_constraint = 1000



def calculate_obj(course_sec_ID, room_timeslot_ID):
    #FIND PENALTY FOR PROF CONSTRAINT
    prof_ID = int(ImportCourseSections.course_sections[course_sec_ID].prof_ID)
    timeslot_ID = InitRoomTimeslots.room_timeslots[room_timeslot_ID].timeslot.ID
    constraint = ImportProfConstraints.prof_constraints[prof_ID][timeslot_ID]

    if constraint == 2:
        obj_value = prof_h_constraint_penalty
    if constraint == 1:
        obj_value = prof_s_constraint_penalty
    else:
        obj_value = 0

    #FIND PENALTY FOR CAPACITY CONSTRAINT
    if InitRoomTimeslots.room_timeslots[room_timeslot_ID].room.capacity < ImportCourseSections.course_sections[course_sec_ID].capacity:
        obj_value += room_capacity_constraint

    return obj_value


def run_optimization():
    #ITERATE THROUGH ALL COURSE SECTIONS TO FIND BEST ROOM TIMESLOT CURRENTLY AVAILABLE
    for x in range(len(ImportCourseSections.course_sections)):
        best_obj = 100000
        for z in range(len(LoadTimeslots.timeslots)):
            for y in range(len(ImportRooms.rooms)):
                room_timeslot_ID = y + z*len(ImportRooms.rooms)
                if(InitRoomTimeslots.room_timeslots[room_timeslot_ID].course_section_ID is False):
                    current_obj = calculate_obj(x, room_timeslot_ID)
                    if current_obj<best_obj:
                        best_obj = current_obj
                        best_room_timeslot_ID = room_timeslot_ID

        #STORE BEST COURSE/ROOM TIMESLOT COMBINATION
        InitRoomTimeslots.room_timeslots[best_room_timeslot_ID].course_section_ID = ImportCourseSections.course_sections[x].ID
        ImportCourseSections.course_sections[x].room_timeslot_ID = best_room_timeslot_ID
        print("SCHEDULING COURSESEC", InitRoomTimeslots.room_timeslots[best_room_timeslot_ID].course_section_ID)
        print("INTO RTS ID", ImportCourseSections.course_sections[x].room_timeslot_ID)
        print("OBJ", calculate_obj(x, best_room_timeslot_ID))